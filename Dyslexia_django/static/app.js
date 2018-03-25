var app = angular.module('quizApp', []);

app.directive('quiz', function(quizFactory) {
	return {
		restrict: 'AE',
		scope: {},
		templateUrl: template,
		
		link: function(scope, elem, attrs) {
			scope.start = function() {
				scope.id = 0;
				scope.quizOver = false;
				scope.inProgress = true;
				quizFactory.serverCall().then(function(){

					scope.getQuestion();
				});

				
				
			};

			scope.reset = function() {
				scope.inProgress = false;
				scope.score = 0;
			}

			scope.getQuestion = function() {
								
				var q = quizFactory.getQuestion(scope.id);
				if(q) {
					scope.question = q.question;
					scope.options = q.options;
					scope.answer = q.answer;
					scope.answerMode = true;
				} else {
					scope.quizOver = true;
                    scope.hits = scope.score;
                    scope.misses = scope.id-scope.score;
                    scope.hitrate = (scope.hits)/scope.id;
					scope.missrate = (scope.misses)/scope.id;
					//scope.Score();	
					//scope.s = scope.score;
				}
			};

			/*scope.Score = function($http) {
				$http.post("http://127.0.0.1:8000/api/results/",
							{
								"res_ID": 1,
								"exam_ID": 'http://127.0.0.1:8000/api/exams/1/',
								"hits": scope.hits,
								"misses": scope.misses,
								"school": scope.accuracy
							})
							.error(function(err){
								console.log(err);
							})
							.success(function(response) 
							{
								console.log("Success")
								console.log(response);
								$scope.usersData = response;
							});
			};*/

			scope.checkAnswer = function() {
				if(!$('input[name=answer]:checked').length) return;

				var ans = $('input[name=answer]:checked').val();

				if(ans == scope.options[scope.answer]) {
					scope.score++;
					scope.correctAns = true;
				} else {
					scope.correctAns = false;
				}

				scope.answerMode = false;
			};

			scope.nextQuestion = function() {
				scope.id++;
				scope.getQuestion();
			}

			scope.reset();
		}
	}
});

app.factory('quizFactory', ['$http',function($http) {
	// var q = [];
	// console.log("Calling API");  
    //     var promise = $http.get("http://127.0.0.1:8000/api/questions");
    //     promise.then(function successCallback(response){
	// 			q = response.data;
	// 			console.log(q);
				

	// 			return {
					
	// 			};

	// 		});

			var questions = [];
			
			return {

				// 1st function
				serverCall: function () {
					return $http.get('http://127.0.0.1:8000/api/questions').then(function (response) {
						
						//var questions = [];
						var qu = response.data;
						questions = [];
						for(var i in qu) {    
							
							var item = qu[i];   
							
							questions.push({ 
								"question" : item.ques,
								"options" : [item.ans1, item.ans2, item.ans3, item.ans4],
								"answer" : item.correct_option					
							});
						}

					});
				},

				
				getQuestion: function(id) {
					console.log(id);
					console.log(questions);

					if(id < questions.length) {
						
						return questions[id];
					} else {
						return false;
					}
				}
			};


}]);