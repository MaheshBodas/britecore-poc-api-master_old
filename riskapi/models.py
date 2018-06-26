from django.contrib.auth.models import User
from django.db import models
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class risktype(models.Model):
    createdby = models.ForeignKey(User, related_name='user_risktypes', on_delete=models.CASCADE,null=True, blank=True)
    risk_type_name = models.CharField(max_length=100, unique=True,
            error_messages={
                'unique': 'risk_type_name must be unique'
            })
    risk_type_description = models.CharField(max_length=100, blank=True, default='')

    def save(self, *args, **kwargs):
        super(risktype, self).save(*args, **kwargs)        

class risktypefield(models.Model):    
    """ risk_type_field_name = models.CharField(max_length=100,unique=True,
            error_messages={
                'unique': 'risk_type_field_name must be unique within and across risk Types'
            }) """
    risk_type_field_name = models.CharField(max_length=100)
    #risk_type_field_enum = EnumChoiceField(enum_class=RiskFieldTypeEnum , default=RiskFieldTypeEnum.text)
    risk_type_field_enum = models.CharField(max_length=10, blank=True, default='')
    risk_type_field_description = models.CharField(max_length=100, blank=True, default='')
    risktype = models.ForeignKey(risktype, related_name='risktype_risktypefields', on_delete=models.CASCADE,null=True, blank=True)    

    # def save(self, *args, **kwargs):
    #     super(risktypefield, self).save(*args, **kwargs)


    

class risk(models.Model):
    createdby = models.ForeignKey(User, related_name='user_risks', on_delete=models.CASCADE,null=True, blank=True)      
    risk_name = models.CharField(max_length=100, unique=True,
            error_messages={
                'unique': 'risk_name must be unique'
            })
    risk_description = models.CharField(max_length=100, blank=True, default='')    
    risktype = models.ForeignKey(risktype,on_delete=models.CASCADE,null=True, blank=True)

    def save(self, *args, **kwargs):
        super(risk, self).save(*args, **kwargs)

    @property
    def risk_type_id(self):
        self.risktype.id
    @property
    def risk_type_name(self):
        self.risktype.risk_type_name

class riskfield(models.Model):
    risk_field_value = models.CharField(max_length=100, blank=True, default='')  
    # Field is of type risktypefield    
    
    risktypefield = models.ForeignKey(risktypefield,on_delete=models.CASCADE,null=True, blank=True)
    risk = models.ForeignKey(risk, related_name='risk_riskfields', on_delete=models.CASCADE,null=True, blank=True)

    """ def save(self, *args, **kwargs):
        super(riskfield, self).save(*args, **kwargs) """

    #   
    @property
    def risk_type_field_id(self):
        self.risktypefield.risk_type_field_id
    @property
    def risk_type_field_name(self):
        self.risktypefield.risk_type_field_name
    @property
    def risk_type_field_enum(self):
        self.risktypefield.risk_type_field_enum
    #        

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(
        choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = models.ForeignKey(
        'auth.User', related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField()

    class Meta:
        ordering = ('created', )

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(
            style=self.style, linenos=linenos, full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)