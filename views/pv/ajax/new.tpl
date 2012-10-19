<form id="new_ajax_pv" action="/pv/ajax/new" method="post">
	<p class="field title">
		<label for="title">Title</label><br />
		<input type="text" name="title" id="title" />
		<br /><span class="error"></span>
	</p>
	<p class="field date">
		<label for="date">Date</label><br />
		<input type="text" name="date" id="date" class="date datepicker" />
		<br /><span class="error"></span>
	</p>
	<p class="field time">
		<label for="time">Time</label><br />
		<input type="text" name="time" id="time" class="time timepicker" />
		<br /><span class="error"></span>
	</p>
	<p class="field location">
		<label for="location">Location</label><br />
		<input type="text" name="location" id="location" />
		<br /><span class="error"></span>
	</p>
	<p class="field description">
		<label for="description">Description</label><br />
		<input type="text" name="description" id="description" />
		<br /><span class="error"></span>
	</p>
</form>