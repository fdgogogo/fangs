angular.module "angular"
.controller "BlogController", (Restangular) ->
  vm = this
  vm.categories = Restangular.all('blog_category').getList().$object
  return vm

