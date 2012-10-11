<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
	<head>
		<script type="text/javascript" src="/js/jquery-1.8.2.js"></script>
		<script type="text/javascript" src="/js/jquery-ui-1.9.0.js"></script>
		<script type="text/javascript" src="/js/jquery-ui-timepicker-addon.js"></script>
		<link rel="stylesheet" href="/css/reset.css" />
		<link rel="stylesheet" href="/css/smoothness/jquery-ui-1.9.0.css" />
		<link rel="stylesheet" href="/css/style.css" />
		<link rel="stylesheet" href="/css/clearfix.css" />
		<script>
			$(function() {
				$('.datepicker').datepicker(
					{
						dateFormat:		"yy-mm-dd",
						changeMonth:	true,
						changeYear:		true,
						showAnim:		"slideDown",
						defaultDate:	null,
						showButtonPanel:true
					}
				);
				$('.timepicker').timepicker({
					timeFormat:	'hh:mm:ss',
					stepHour:	1,
					stepMinute:	5,
					showAnim:	"slideDown",
				});
			});
		</script>
		<title>{{!title}}</title>
	</head>
	<body>
		%include
	</body>
</html>