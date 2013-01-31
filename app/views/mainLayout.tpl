<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8" />
	<title>{{title}} // Bottle (Python) Bootstrap</title>
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<meta name="description" content="" />
	<meta name="author" content="" />

	<!--CSS-START-->
	<link href="/resources/css/bootstrap.css" rel="stylesheet" />
	<link href="/resources/css/bootstrap-responsive.css" rel="stylesheet" />
	<link href="/resources/css/style.css" rel="stylesheet" />
	<!--CSS-END-->

	<!--[if lt IE 9]>
	<script src="/resources/js/html5.js"></script>
	<![endif]-->
</head>

<body>
	<div class="navbar navbar-inverse navbar-fixed-top">
		<div class="navbar-inner">
			<div class="container-fluid">
				<a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
				</a>
				<a class="brand" href="#">Bottle (Python) Bootstrap</a>
				<div class="nav-collapse collapse">
					<p class="navbar-text pull-right">
						Logged in as <a href="#" class="navbar-link">Username</a>
					</p>
					
					<ul class="nav">
						<li class="active"><a href="#">Home</a></li>
						<li><a href="#about">About</a></li>
						<li><a href="#contact">Contact</a></li>
					</ul>
				</div>
			</div>
		</div>
	</div>

	<div class="container-fluid">
		<div class="row-fluid">
			<div class="span3">
				<div class="well sidebar-nav">
					<ul class="nav nav-list">
						<li class="nav-header">Sidebar</li>
						<li class="active"><a href="#">Link</a></li>
						<li><a href="#">Link</a></li>
						<li><a href="#">Link</a></li>
						<li><a href="#">Link</a></li>
						<li class="nav-header">Sidebar</li>
						<li><a href="#">Link</a></li>
						<li><a href="#">Link</a></li>
						<li><a href="#">Link</a></li>
						<li><a href="#">Link</a></li>
						<li><a href="#">Link</a></li>
						<li><a href="#">Link</a></li>
						<li class="nav-header">Sidebar</li>
						<li><a href="#">Link</a></li>
						<li><a href="#">Link</a></li>
						<li><a href="#">Link</a></li>
					</ul>
				</div><!--/.well -->
			</div><!--/span-->

			<div class="span9">
				<div class="hero-unit">
					<h1>Hello, world!</h1>
					<p>
						This is my Bottle (Python) Bootstrapper. I use this to quickly startup a Python web-application
						using Bottlepy, jQuery, Twitter Bootstrap, Beaker session management, and SQLAlchemy.
					</p>
					
					<p>
						<a class="btn btn-primary btn-large">Learn more &raquo;</a>
					</p>
				</div>

				<!--JS-START-->
				<script src="/resources/js/jquery.js"></script>
				<!--JS-END-->
				
				<!-- CONTENT -->
				<div class="row-fluid">
					<div class="span12" id="contentContainer">
						%include
					</div>
				</div>
				<!-- END-CONTENT -->
			</div><!--/span-->
		</div><!--/row-->

		<hr>

		<footer>
			<p>&copy; Company 2012</p>
		</footer>
	</div><!--/.fluid-container-->
</body>
</html>