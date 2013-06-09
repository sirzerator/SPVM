		<div class="header clearfix">
			<div class="spvm"><h1>SPVM</h1></div>
			<div class="title"><h2>{{pv_data['title']}}</h2></div>
			<div class="controls">
				<ul class="icons ui-widget ui-helper-clearfix">
					<li class="ui-state-default ui-corner-all"><a title="Configure" class="pv config" href="/pv/config"><span class="ui-icon ui-icon-wrench"></span></a></li>
					<li class="ui-state-default ui-corner-all"><a title="Close" class="pv close" href="/pv/close"><span class="ui-icon ui-icon-close"></span></a></li>
				</ul>
			</div>
		</div>
		<div class="informations toggle horizontal">
			<div class="button over"></div>
			<div class="content">
				<p class="title">Informations</p>
				<p class="location">{{pv_data['location']}}</p>
				<p class="date time">{{pv_data['date']}} {{pv_data['time']}}</p>
				<p class="description">{{pv_data['description']}}</p>
				<p class="modified">{{pv_data['modified']}}</p>
			</div>
		</div>
		<script type="text/javascript">
			$(document).ready(function() {
				assignButtonElements($('body'));
			});
		</script>
		<div class="left panel">
			%include main_left points=points
		</div>
		<div class="right panel">
			%include main_right participants=participants, pv_id=pv_id
		</div>
		<div class="footer clearfix">
			<div class="status"><p>Status bar</p></div>
		</div>
		%rebase html title=pv_data['title'] + ' &mdash; SPVM'