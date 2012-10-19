		<h1>SPVM</h1>
		<h2>PVs</h2>
		<table class="pv">
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
				<tr id="pv_{{id}}">
					<td>{{id}}</td>
					<td><a href="/pv/select/{{id}}">{{title}}</a></td>
					<td>{{date}}</td>
					<td>{{time}}</td>
					<td>{{location}}</td>
					<td>{{description}}</td>
					<td><ul class="icons ui-widget ui-helper-clearfix"><li class="ui-state-default ui-corner-all"><a href="/pv/edit/{{id}}" title="Edit"><span class="ui-icon ui-icon-pencil"></span></a></li><li class="ui-state-default ui-corner-all"><a href="/pv/delete/{{id}}" title="Delete"><span class="ui-icon ui-icon-trash"></span></a></li></ul></td>
				</tr>
				%end
				<tr class="overflow" id="pv_*|id|*">
					<td>*|id|*</td>
					<td><a href="/pv/select/*|id|*">*|title|*</a></td>
					<td>*|date|*</td>
					<td>*|time|*</td>
					<td>*|location|*</td>
					<td>*|description|*</td>
					<td><ul class="icons ui-widget ui-helper-clearfix"><li class="ui-state-default ui-corner-all"><a href="/pv/edit/*|id|*" title="Edit"><span class="ui-icon ui-icon-pencil"></span></a></li><li class="ui-state-default ui-corner-all"><a href="/pv/delete/*|id|*" title="Delete"><span class="ui-icon ui-icon-trash"></span></a></li></ul></td>
				</tr>
			%else:
				<tr>
					<td colspan="7">Nothing to display.</td>
				</tr>
			%end
			</tbody>
		</table>
		<a href="/pv/new" class="button add pv"><button>New PV</button></a>
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
							$('#dialog .error').html('');
							$.ajax("/pv/ajax/new", {
								type: 'post',
								data: {
									'title': $('#title').val(),
									'date': $('#date').val(),
									'time': $('#time').val(),
									'location': $('#location').val(),
									'description': $('#description').val()
								}
							}).done(function(response) {
								if (response['id']) {
									$("#dialog").dialog("close");
									string = '<tr id="pv_' + response['id'] + '">';
									string += '<td>' + response['id'] + '</td>';
									string += '<td><a href="/pv/select/' + response['id'] +'">' + $('#title').val() + '</a></td>';
									string += '<td>' + $('#date').val() + '</td>';
									string += '<td>' + $('#time').val() + '</td>';
									string += '<td>' + $('#location').val() + '</td>';
									string += '<td>' + $('#description').val() + '</td>';
									string += '<td><ul class="icons ui-widget ui-helper-clearfix"><li class="ui-state-default ui-corner-all"><a href="/pv/edit/' + response['id'] + '" title="Edit"><span class="ui-icon ui-icon-pencil"></span></a></li><li class="ui-state-default ui-corner-all"><a href="/pv/delete/' + response['id'] + '" title="Delete"><span class="ui-icon ui-icon-trash"></span></a></li></ul></td>';
									string += '</tr>';
									$("table.pv tbody").append(string);
									$("#dialog").dialog("close");
								} else {
									if (response['title']) {
										$('.title .error').html(response['title']);
									}
									if (response['date']) {
										$('.date .error').html(response['date']);
									}
									if (response['time']) {
										$('.time .error').html(response['time']);
									}
								}
							});
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
					$("#dialog").load("/pv/ajax/new", null, function() {
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