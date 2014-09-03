(function() {
	var app = angular.module('HomeController', []);

	app.controller('MainController', function($scope, $http, computerList, booter) {
		computerList.getComputers().success(function(data) {
			$scope.computers = data;
		});

		$scope.boot = function(computer) {
			booter.boot(computer);
		};
	});

	app.factory('computerList', function($http) {
		return {
			getComputers: function() {
				return $http.get('/computers');
			}
		}
	});

	app.service('booter', function($http) {
		this.boot = function(computer) {
			$http.get('/boot/'+computer);
		};
	});
})();