var app = angular.module('MyApp',[]);
app.controller('registerController',function($scope,$http) {
    $scope.Register = function() {
        $http.post("http://127.0.0.1:8000/api/patients/",
        {
            "first_name": $scope.fn,
            "last_name": $scope.ln,
            "age": $scope.age,
            "p_dob": $scope.dob,
            "school": $scope.s,
            "grade": $scope.g,
            "password": $scope.pwd,
            "p_email": $scope.email
        })
        .error(function(err){
            console.log(err);
        })
        .success(function(response) 
        {
            console.log("Success")
            console.log(response);
            //$scope.usersData = response;
        });
    };
});