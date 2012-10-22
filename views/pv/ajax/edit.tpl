<form id="pv_ajax_edit" action="/pv/ajax/edit" method="post">
	<input type="hidden" name="pv_id" id="pv_id" value="{{data['id']}}" />
	<p class="field title">
		<label for="title">Title</label><br />
		<input class="text ui-widget-content ui-corner-all" type="text" name="title" id="title" value="{{data['title']}}" />
		<br /><span class="error"></span>
	</p>
	<p class="field date">
		<label for="date">Date</label><br />
		<input class="date datepicker ui-widget-content ui-corner-all" type="text" name="date" id="date" value="{{data['date']}}" />
		<br /><span class="error"></span>
	</p>
	<p class="field time">
		<label for="time">Time</label><br />
		<input class="time timepicker ui-widget-content ui-corner-all" type="text" name="time" id="time" value="{{data['time']}}" />
		<br /><span class="error"></span>
	</p>
	<p class="field location">
		<label for="location">Location</label><br />
		<input class="text ui-widget-content ui-corner-all" type="text" name="location" id="location"value="{{data['location']}}" />
		<br /><span class="error"></span>
	</p>
	<p class="field description">
		<label for="description">Description</label><br />
		<input class="text ui-widget-content ui-corner-all" type="text" name="description" id="description" value="{{data['description']}}" />
		<br /><span class="error"></span>
	</p>
</form>