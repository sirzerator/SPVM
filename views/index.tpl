		<h1>SPVM</h1>
		<h2>PVs</h2>
		<table>
			<thead>
				<th>#</th>
				<th>Titre</th>
				<th>Date</th>
				<th>Time</th>
				<th>Location</th>
				<th>Description</th>
				<th>Actions</th>
			</thead>
			<tbody>
			%if pvs['count']:
				%for id, user_id, title, date, time, location, description, code_id, lock_id, created, modified in pvs['rows']:
				<tr>
					<td>{{id}}</td>
					<td><a href="/pvs/select/{{id}}">{{title}}</a></td>
					<td>{{date}}</td>
					<td>{{time}}</td>
					<td>{{location}}</td>
					<td>{{description}}</td>
					<td><ul class="icons ui-widget ui-helper-clearfix"><li class="ui-state-default ui-corner-all"><a href="/pvs/edit/{{id}}" title="Edit"><span class="ui-icon ui-icon-pencil"></span></a></li><li class="ui-state-default ui-corner-all"><a href="/pvs/delete/{{id}}" title="Delete"><span class="ui-icon ui-icon-trash"></span></a></li></ul></td>
				</tr>
				%end
			%else:
				<tr>
					<td colspan="7">Nothing to display.</td>
				</tr>
			%end
			</tbody>
		</table>
		<a href="/pvs/new" class="button add pv"><button>New PV</button></a>
		<div id="dialog" title="New PV"></div>
		<script type="text/javascript">
			$(document).ready(function() {
				$("#dialog").dialog({
					autoOpen: false,
					height: 330,
					width: 200,
					modal: true,
					buttons: {
						"New PV": function() {
							$("#dialog").dialog("close");
						},
						Cancel: function() {
							$("#dialog").dialog("close");
						}
					},
					close: function() {
						$(this).dialog("close");
					}
				});
				$(".pv.add").click(function(e) {
					e.preventDefault();
					$("#dialog").load("/pvs/ajax/new", null, function() {
						$('.datepicker').datepicker(
							{
								dateFormat: "yy-mm-dd",
								changeMonth: true,
								changeYear: true,
								showAnim: "slideDown",
								defaultDate: new Date(),
								showButtonPanel: true,
								showOtherMonths: true,
								selectOtherMonths: true
							}
						);
						$('.timepicker').timepicker({
							timeFormat:	'hh:mm:ss',
							stepHour: 1,
							stepMinute: 5,
							defaultTime: 0,
							showAnim: "slideDown",
						});
						$('ul.icons li').hover(
							function() { $(this).addClass('ui-state-hover'); },
							function() { $(this).removeClass('ui-state-hover'); }
						);
					});
					$("#dialog").dialog("open");
				});
			});
		</script>
		%rebase layout title='SPVM'