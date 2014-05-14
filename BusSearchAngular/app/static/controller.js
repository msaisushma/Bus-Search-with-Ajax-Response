'use strict';
// var busApp = angular.module('busApp', []);

// busApp.controller('BusRouteCtrl', ['$scope', '$http',
	// function ($scope,$http) {
 	// $http.get('/busroutes/').success(function(data){
		// $scope.busroutes = data;
// });
// });

 var busApp = angular.module('busApp', []);

 busApp.controller('BusRouteCtrl', function ($scope) {


 $scope.busroutes = [
 {'Bus_no': 210,
 'Start_point':'Majestic',
 'End_point':'Uttarahalli',
 'Route_info': 'Chamrajpet Lalbagh NR Colony'},

 {'Bus_no': 3,
 'Start_point':'Banashankari 3rd stage',
 'End_point':'BTM layout',
 'Route_info': 'GandhiBazaar Jayanagar 4th block EastEnd BTMLayout'},

 {'Bus_no': 77,
 'Start_point':'NRColony',
 'End_point':'Mahalakshmi Layout',
 'Route_info': 'Netkallappacircle Chamrajpet Navrang Sujatha'}
 ];
 });
