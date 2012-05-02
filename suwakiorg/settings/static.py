PIPELINE_CSS = {
    'all': {
        'source_filenames': (
            'css/base.scss',
            'css/suwaki.scss',
            'css/ui-lightness/jquery-ui-1.8.18.custom.css',
        ),
        'output_filename': 'css/all.css',
    },
}

PIPELINE_JS = {
    'all': {
        'source_filenames': (
          'js/jquery-ui-1.8.18.custom.min.js',
          'js/suwaki.js',
        ),
        'output_filename': 'js/all.js',
    }
}

PIPELINE_CSS_COMPRESSOR = None
PIPELINE_JS_COMPRESSOR = None

PIPELINE_COMPILERS = (
    'pipeline_scss.SCSSCompiler',
)
#PIPELINE_STORAGE = 'pipeline.storage.PipelineFinderStorage'
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

#STATICFILES_FINDERS = (
#   'pipeline.finders.PipelineFinder',
#   'django.contrib.staticfiles.finders.FileSystemFinder',
#   'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#)
