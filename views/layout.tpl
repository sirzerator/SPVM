<html>
	<head>
		<script type="text/javascript" src="/js/jquery-1.8.2.js"></script>
		<script type="text/javascript" src="/js/jquery-ui-1.9.0.js"></script>
		<script type="text/javascript" src="/js/jquery-ui-timepicker-addon.js"></script>
		<link rel="stylesheet" href="/css/smoothness/jquery-ui-1.9.0.css" />
		<script>
			$(function() {
				$('.datepicker').datepicker(
					{
						"dateFormat":	"yy-mm-dd",
						"changeMonth":	true,
						"changeYear":	true,
						"showAnim":		"slideDown",
						"defaultDate":	null,
						"showButtonPanel":	true
					}
				);
				$('.timepicker').timepicker({
					timeFormat: 'hh:mm:ss',
					stepHour: 1,
					stepMinute: 5
				});
			});
		</script>
		<title>{{!title}}</title>
	</head>
	<body>
		%include
	</body>
</html>