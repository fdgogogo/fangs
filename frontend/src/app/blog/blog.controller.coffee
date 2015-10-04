angular.module "angular"
.controller "BlogController", (Restangular, $location) ->
  vm = this
  vm.categories = Restangular.all('blog_category').getList().$object
  vm.jumpToCategory = (slug) ->
    $location.path('/blog/categories/' + slug)
  return vm

