# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-05-02 01:27
from django.db import migrations, models

import readthedocs.projects.validators


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0023_migrate-alias-slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='show_version_warning',
            field=models.URLField(blank=True, help_text='You are seeing unstable version of the documentation, see the stable versions.', verbose_name='Show version warning'),
        ),
        migrations.AlterField(
            model_name='domain',
            name='canonical',
            field=models.BooleanField(default=False, help_text='This Domain is the primary one where the documentation is served from'),
        ),
        migrations.AlterField(
            model_name='domain',
            name='count',
            field=models.IntegerField(default=0, help_text='Number of times this domain has been hit'),
        ),
        migrations.AlterField(
            model_name='project',
            name='allow_promos',
            field=models.BooleanField(default=True, help_text='If unchecked, users will still see community ads.', verbose_name='Allow paid advertising'),
        ),
        migrations.AlterField(
            model_name='project',
            name='conf_py_file',
            field=models.CharField(blank=True, default='', help_text='Path from project root to <code>conf.py</code> file (ex. <code>docs/conf.py</code>). Leave blank if you want us to find it for you.', max_length=255, verbose_name='Python configuration file'),
        ),
        migrations.AlterField(
            model_name='project',
            name='default_version',
            field=models.CharField(default='latest', help_text='The version of your project that / redirects to', max_length=255, verbose_name='Default version'),
        ),
        migrations.AlterField(
            model_name='project',
            name='documentation_type',
            field=models.CharField(choices=[('auto', 'Automatically Choose'), ('sphinx', 'Sphinx Html'), ('mkdocs', 'Mkdocs (Markdown)'), ('sphinx_htmldir', 'Sphinx HtmlDir'), ('sphinx_singlehtml', 'Sphinx Single Page HTML')], default='sphinx', help_text='Type of documentation you are building. <a href="http://sphinx-doc.org/builders.html#sphinx.builders.html.DirectoryHTMLBuilder">More info</a>.', max_length=20, verbose_name='Documentation type'),
        ),
        migrations.AlterField(
            model_name='project',
            name='has_valid_webhook',
            field=models.BooleanField(default=False, help_text='This project has been built with a webhook'),
        ),
        migrations.AlterField(
            model_name='project',
            name='language',
            field=models.CharField(choices=[('aa', 'Afar'), ('ab', 'Abkhaz'), ('af', 'Afrikaans'), ('am', 'Amharic'), ('ar', 'Arabic'), ('as', 'Assamese'), ('ay', 'Aymara'), ('az', 'Azerbaijani'), ('ba', 'Bashkir'), ('be', 'Belarusian'), ('bg', 'Bulgarian'), ('bh', 'Bihari'), ('bi', 'Bislama'), ('bn', 'Bengali'), ('bo', 'Tibetan'), ('br', 'Breton'), ('ca', 'Catalan'), ('co', 'Corsican'), ('cs', 'Czech'), ('cy', 'Welsh'), ('da', 'Danish'), ('de', 'German'), ('dz', 'Dzongkha'), ('el', 'Greek'), ('en', 'English'), ('eo', 'Esperanto'), ('es', 'Spanish'), ('et', 'Estonian'), ('eu', 'Basque'), ('fa', 'Iranian'), ('fi', 'Finnish'), ('fj', 'Fijian'), ('fo', 'Faroese'), ('fr', 'French'), ('fy', 'Western Frisian'), ('ga', 'Irish'), ('gd', 'Scottish Gaelic'), ('gl', 'Galician'), ('gn', 'Guarani'), ('gu', 'Gujarati'), ('ha', 'Hausa'), ('hi', 'Hindi'), ('he', 'Hebrew'), ('hr', 'Croatian'), ('hu', 'Hungarian'), ('hy', 'Armenian'), ('ia', 'Interlingua'), ('id', 'Indonesian'), ('ie', 'Interlingue'), ('ik', 'Inupiaq'), ('is', 'Icelandic'), ('it', 'Italian'), ('iu', 'Inuktitut'), ('ja', 'Japanese'), ('jv', 'Javanese'), ('ka', 'Georgian'), ('kk', 'Kazakh'), ('kl', 'Kalaallisut'), ('km', 'Khmer'), ('kn', 'Kannada'), ('ko', 'Korean'), ('ks', 'Kashmiri'), ('ku', 'Kurdish'), ('ky', 'Kyrgyz'), ('la', 'Latin'), ('ln', 'Lingala'), ('lo', 'Lao'), ('lt', 'Lithuanian'), ('lv', 'Latvian'), ('mg', 'Malagasy'), ('mi', 'Maori'), ('mk', 'Macedonian'), ('ml', 'Malayalam'), ('mn', 'Mongolian'), ('mr', 'Marathi'), ('ms', 'Malay'), ('mt', 'Maltese'), ('my', 'Burmese'), ('na', 'Nauru'), ('ne', 'Nepali'), ('nl', 'Dutch'), ('no', 'Norwegian'), ('oc', 'Occitan'), ('om', 'Oromo'), ('or', 'Oriya'), ('pa', 'Panjabi'), ('pl', 'Polish'), ('ps', 'Pashto'), ('pt', 'Portuguese'), ('qu', 'Quechua'), ('rm', 'Romansh'), ('rn', 'Kirundi'), ('ro', 'Romanian'), ('ru', 'Russian'), ('rw', 'Kinyarwanda'), ('sa', 'Sanskrit'), ('sd', 'Sindhi'), ('sg', 'Sango'), ('si', 'Sinhala'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('sm', 'Samoan'), ('sn', 'Shona'), ('so', 'Somali'), ('sq', 'Albanian'), ('sr', 'Serbian'), ('ss', 'Swati'), ('st', 'Southern Sotho'), ('su', 'Sudanese'), ('sv', 'Swedish'), ('sw', 'Swahili'), ('ta', 'Tamil'), ('te', 'Telugu'), ('tg', 'Tajik'), ('th', 'Thai'), ('ti', 'Tigrinya'), ('tk', 'Turkmen'), ('tl', 'Tagalog'), ('tn', 'Tswana'), ('to', 'Tonga'), ('tr', 'Turkish'), ('ts', 'Tsonga'), ('tt', 'Tatar'), ('tw', 'Twi'), ('ug', 'Uyghur'), ('uk', 'Ukrainian'), ('ur', 'Urdu'), ('uz', 'Uzbek'), ('vi', 'Vietnamese'), ('vo', 'Volapuk'), ('wo', 'Wolof'), ('xh', 'Xhosa'), ('yi', 'Yiddish'), ('yo', 'Yoruba'), ('za', 'Zhuang'), ('zh', 'Chinese'), ('zu', 'Zulu'), ('nb_NO', 'Norwegian Bokmal'), ('pt_BR', 'Brazilian Portuguese'), ('uk_UA', 'Ukrainian'), ('zh_CN', 'Simplified Chinese'), ('zh_TW', 'Traditional Chinese')], default='en', help_text="The language the project documentation is rendered in. Note: this affects your project's URL.", max_length=20, verbose_name='Language'),
        ),
        migrations.AlterField(
            model_name='project',
            name='privacy_level',
            field=models.CharField(choices=[('public', 'Public'), ('protected', 'Protected'), ('private', 'Private')], default='public', help_text='(Beta) Level of privacy that you want on the repository. Protected means public but not in listings.', max_length=20, verbose_name='Privacy Level'),
        ),
        migrations.AlterField(
            model_name='project',
            name='programming_language',
            field=models.CharField(blank=True, choices=[('words', 'Only Words'), ('py', 'Python'), ('js', 'JavaScript'), ('php', 'PHP'), ('ruby', 'Ruby'), ('perl', 'Perl'), ('java', 'Java'), ('go', 'Go'), ('julia', 'Julia'), ('c', 'C'), ('csharp', 'C#'), ('cpp', 'C++'), ('objc', 'Objective-C'), ('css', 'CSS'), ('ts', 'TypeScript'), ('swift', 'Swift'), ('vb', 'Visual Basic'), ('r', 'R'), ('scala', 'Scala'), ('groovy', 'Groovy'), ('coffee', 'CoffeeScript'), ('lua', 'Lua'), ('haskell', 'Haskell'), ('other', 'Other')], default='words', help_text='The primary programming language the project is written in.', max_length=20, verbose_name='Programming Language'),
        ),
        migrations.AlterField(
            model_name='project',
            name='python_interpreter',
            field=models.CharField(choices=[('python', 'CPython 2.x'), ('python3', 'CPython 3.x')], default='python', help_text='(Beta) The Python interpreter used to create the virtual environment.', max_length=20, verbose_name='Python Interpreter'),
        ),
        migrations.AlterField(
            model_name='project',
            name='repo',
            field=models.CharField(help_text='Hosted documentation repository URL', max_length=255, validators=[readthedocs.projects.validators.RepositoryURLValidator()], verbose_name='Repository URL'),
        ),
        migrations.AlterField(
            model_name='project',
            name='repo_type',
            field=models.CharField(choices=[('git', 'Git'), ('svn', 'Subversion'), ('hg', 'Mercurial'), ('bzr', 'Bazaar')], default='git', max_length=10, verbose_name='Repository type'),
        ),
        migrations.AlterField(
            model_name='project',
            name='suffix',
            field=models.CharField(default='.rst', editable=False, max_length=10, verbose_name='Suffix'),
        ),
        migrations.AlterField(
            model_name='project',
            name='theme',
            field=models.CharField(choices=[('default', 'Default'), ('sphinxdoc', 'Sphinx Docs'), ('traditional', 'Traditional'), ('nature', 'Nature'), ('haiku', 'Haiku')], default='default', help_text='<a href="http://sphinx.pocoo.org/theming.html#builtin-themes" target="_blank">Examples</a>', max_length=20, verbose_name='Theme'),
        ),
        migrations.AlterField(
            model_name='project',
            name='version_privacy_level',
            field=models.CharField(choices=[('public', 'Public'), ('protected', 'Protected'), ('private', 'Private')], default='public', help_text='(Beta) Default level of privacy you want on built versions of documentation.', max_length=20, verbose_name='Version Privacy Level'),
        ),
    ]
