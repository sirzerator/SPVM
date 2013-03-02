<form id="point_ajax_new" action="/point/ajax/new" method="post">
	<input type="hidden" id="pv_id" name="pv_id" value="{{pv_id}}" />
	<p class="field title">
		<label for="title">Title</label><br />
		<input class="text ui-widget-content ui-corner-all" type="text" name="title" id="title" />
		<br /><span class="error"></span>
	</p>
	<p class="field description">
		<label for="description">Description</label><br />
		<input class="text ui-widget-content ui-corner-all" type="text" name="description" id="description" />
		<br /><span class="error"></span>
	</p>
	<p class="field rank">
		<label for="rank">Rank</label><br />
		<input class="text ui-widget-content ui-corner-all" type="text" name="rank" id="rank" />
		<br /><span class="error"></span>
	</p>
	<p class="field parent">
		<label for="parent_id">Parent</label><br />
		<select id="parent_id" name="parent_id">
			<option value="">---</option>
			%if points['count']:
				%for point in points['rows']:
					<option value="{{point['id']}}">{{point['title']}}</option>
				%end
			%end
		</select>
	</p>
</form>