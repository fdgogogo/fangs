angular.module "angular"
.config ($logProvider, toastr, $locationProvider, RestangularProvider, $mdThemingProvider) ->
  # Enable log
  $logProvider.debugEnabled true
  # Set options third-party lib
  toastr.options.timeOut = 3000
  toastr.options.positionClass = 'toast-top-right'
  toastr.options.preventDuplicates = true
  toastr.options.progressBar = true
  $locationProvider.html5Mode(
    enabled: true
    requireBase: true
  ).hashPrefix('!')

  RestangularProvider.setBaseUrl('http://localhost:5000/api/v1')
  RestangularProvider.addResponseInterceptor (data, operation, what, url, response, deferred) ->
    extractedData = undefined
    if operation == 'getList'

      extractedData = data['objects']

      meta = angular.copy(data)
      delete meta['objects']
      extractedData['meta'] = meta
    else
      extractedData = data
    extractedData

  $mdThemingProvider.theme('default')
    .primaryPalette('indigo')
    .accentPalette('blue')

