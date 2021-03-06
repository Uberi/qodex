<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<meta name="description" content="qodex home page">
		<meta name="author" content="Keri Warr">

		<title>qödex</title>

		<!-- Bootstrap core CSS -->
		<link href="../css/bootstrap.min.css" rel="stylesheet">

		<!-- Custom styles for this template -->
		<link href="../starter-template.css" rel="stylesheet">

		<link href='http://fonts.googleapis.com/css?family=Roboto+Slab:700' rel='stylesheet' type='text/cs
		
		<!-- Just for debugging purposes. Don't actually copy this line! -->
		<!--[if lt IE 9]><script src="../../assets/js/ie8-responsive-file-warning.js"></script><![endif]-->

		<!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
		<!--[if lt IE 9]>
			<script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
			<script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
		<![endif]-->
		
		<style>
		td {
			padding: 1em !important;
			font-size: 2em;
		}
		</style>
	</head>

	<body>
		<div class="navbar navbar-inverse  navbar-fixed-top" role="navigation">
			<div class="container">
				<div class="navbar-header">
					<button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
						<span class="sr-only">Toggle navigation</span>
						<span class="icon-bar"></span>
						<span class="icon-bar"></span>
						<span class="icon-bar"></span>
					</button>
					<a id="logo" class="navbar-brand" href="#">qödex</a>
				</div>
				<div class="collapse navbar-collapse">
					<ul class="nav navbar-nav">
						<li><a class="menu" href=".."><div class="glyphicon glyphicon-home"></div>Home</a></li>
						<li class="active"><a class="menu" href="#"><div class="glyphicon glyphicon-user"></div>Profile</a></li>
						<li><a class="menu" href="../groups"><div class="glyphicon glyphicon-comment"></div>Groups</a></li>
					</ul>
				</div>
			</div>
		</div>
	

	
		<div class="background">
			<div class="background-top"></div>
		</div>

		<article>
			<div class="horizontal-buffer"></div>
			<h2 style="text-align:center;border-bottom:3px solid #333;padding-bottom:20px">${user_name}'s Profile</h2>
			<div class="horizontal-buffer"></div>
			<div class="panel panel-default">
				<!-- Default panel contents -->
				<div class="panel-heading">Details</div>

				<!-- Table -->
				<table class="table">
				    <tr>
						<td>Username:</td>
						<td>${user_name}</td>
						<td><button class="btn btn-warning">Change <i class="glyphicon-white glyphicon-pencil"></i></button></td>
					</tr>
					<tr>
						<td>E-mail:</td>
						<td>${user_email}</td>
						<td><button class="btn btn-warning">Change <i class="glyphicon-white glyphicon-pencil"></i></button></td>
					</tr>
					<tr>
						<td>Password</td>
						<td>********</td>
						<td><button class="btn btn-warning">Change <i class="glyphicon-white glyphicon-pencil"></i></button></td>
					</tr>
				</table>
			</div>
		</article>

		<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
		<script src="../../dist/js/bootstrap.min.js"></script>
	</body>
</html>
