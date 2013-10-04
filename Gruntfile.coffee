module.exports = ->
  # Project configuration
  @initConfig
    pkg: @file.readJSON 'package.json'
    exec:
      test:
        command: 'python rpsrunner.py -t 2 bots/*.py'
    watch:
      files: ['bots/*.py']
      tasks: ['test']

  # Grunt plugins used for building
  @loadNpmTasks 'grunt-exec'
  @loadNpmTasks 'grunt-contrib-watch'

  # Our local tasks
  @registerTask 'test', ['exec']
  @registerTask 'default', ['test']