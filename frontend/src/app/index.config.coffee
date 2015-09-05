angular.module "angular"
  .config ($logProvider, toastr, $locationProvider, RestangularProvider) ->
    # Enable log
    $logProvider.debugEnabled true
    # Set options third-party lib
    toastr.options.timeOut = 3000
    toastr.options.positionClass = 'toast-top-right'
    toastr.options.preventDuplicates = true
    toastr.options.progressBar = true
    $locationProvider.html5Mode(
      enabled: true
      requireBase: false
    ).hashPrefix('!')
    RestangularProvider.setBaseUrl('http://localhost:5000/api/v1')
