// Karma configuration file, see link for more information
// https://karma-runner.github.io/0.13/config/configuration-file.html
var path = require('path');

module.exports = function (config) {
  config.set({
    basePath: '',
    frameworks: ['jasmine', '@angular/cli'],
    plugins: [
      require('karma-jasmine'),
      require('karma-chrome-launcher'),
      require('karma-jasmine-html-reporter'),
      require('karma-coverage-istanbul-reporter'),
      require('karma-teamcity-reporter'),
      require('@angular/cli/plugins/karma'),
      require('karma-phantomjs-launcher')
    ],
    reporters: ['teamcity', 'coverage-istanbul'],
    client:{
      clearContext: false // leave Jasmine Spec Runner output visible in browser
    },
    coverageIstanbulReporter: {
      reports: [ 'html', 'teamcity' ],
      dir: path.join(__dirname, 'coverage'),
      fixWebpackSourcePaths: true,
      includeAllSources: true
    },
    angularCli: {
      environment: 'dev'
    },
    port: 9876,
    colors: true,
    logLevel: config.LOG_INFO,
    autoWatch: true,
    browsers: ['PhantomJS'],
    singleRun: true
  });
};
