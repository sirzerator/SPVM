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
				%for row in pvs['rows']:
				<tr id="pv_{{row['id']}}">
					<td>{{row['id']}}</td>
					<td><a href="/pv/select/{{row['id']}}">{{row['title']}}</a></td>
					<td>{{row['date']}}</td>
					<td>{{row['time']}}</td>
					<td>{{row['location']}}</td>
					<td>{{row['description']}}</td>
					<td>
						<ul class="icons ui-widget ui-helper-clearfix">
							<li class="ui-state-default ui-corner-all"><a href="/pv/edit/{{row['id']}}" class="pv edit" rel="{{row['id']}}" title="Edit"><span class="ui-icon ui-icon-pencil"></span></a></li>
							<li class="ui-state-default ui-corner-all"><a href="/pv/delete/{{row['id']}}" class="pv delete" rel="{{row['id']}}" title="Delete"><span class="ui-icon ui-icon-trash"></span></a></li>
						</ul>
					</td>
				</tr>
				%end
			%else:
				<tr class="nothing">
					<td colspan="7">Nothing to display.</td>
				</tr>
			%end
				<tr class="overflow">
					<td>*|id|*</td>
					<td><a href="/pv/select/*|id|*">*|title|*</a></td>
					<td>*|date|*</td>
					<td>*|time|*</td>
					<td>*|location|*</td>
					<td>*|description|*</td>
					<td><ul class="icons ui-widget ui-helper-clearfix"><li class="ui-state-default ui-corner-all"><a href="/pv/edit/*|id|*" class="pv edit" rel="*|id|*" title="Edit"><span class="ui-icon ui-icon-pencil"></span></a></li><li class="ui-state-default ui-corner-all"><a href="/pv/delete/*|id|*" class="pv delete" rel="*|id|*" title="Delete"><span class="ui-icon ui-icon-trash"></span></a></li></ul></td>
				</tr>
			</tbody>
		</table>
		<a href="/pv/new" class="button new pv"><button class="ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only"><span class="ui-button-text">New PV</span></button></a>
		<script type="text/javascript">
			$(document).ready(function() {
				assignButtonElements($('body'));
				$(".pv.new").click(function(e) {
					e.preventDefault();
					properties = {
						title:"New PV",
						OK:"Create",
						Cancel:"Cancel",
						width:200,
						height:330,
						modal:true,
						resizable:false,
						beforeClose: function() {}
					}
					castDialog('pv', 'new', properties, null);
				});
				$("table.pv").delegate(".pv.delete", "click", function(e) {
					e.preventDefault();
					castDialog('pv', 'delete', {title:"Are you sure you want to delete this PV ?", OK:"Yes", Cancel:"No", width:300, height:125, modal:true, resizable:false}, "pv_id=" + $(this).attr('rel'));
				});
				$(".pv.edit").click(function(e) {
					e.preventDefault();
					properties = {
						title:"Edit PV",
						OK:"Edit",
						Cancel:"Cancel",
						width:200,
						height:330,
						modal:true,
						resizable:false,
						beforeClose: function() {}
					}
					castDialog('pv', 'edit', properties, "pv_id=" + $(this).attr('rel'));
				});
			});
		</script>
		%rebase layout title='SPVM'