angular.module "angular"
.controller "MainController", ($timeout, webDevTec, toastr) ->
  vm = this
  activate = ->
    getWebDevTec()
    $timeout (->
      vm.classAnimation = 'rubberBand'
    ), 4000

  showToastr = ->
    toastr.info 'Fork <a href="https://github.com/Swiip/generator-gulp-angular" target="_blank"><b>generator-gulp-angular</b></a>'
    vm.classAnimation = ''

  getWebDevTec = ->
    vm.awesomeThings = webDevTec.getTec()
    angular.forEach vm.awesomeThings, (awesomeThing) ->
      awesomeThing.rank = Math.random()

  vm.awesomeThings = []
  vm.classAnimation = ''
  vm.creationDate = 1441371210288
  vm.showToastr = showToastr
  activate()
  return vm
