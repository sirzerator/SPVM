<form id="pv_edit" action="/pv/edit" method="post">
	<input type="hidden" name="pv_id" id="pv_id" value="{{data['id']}}" />
	<p class="field title">
		<label for="title">Title</label><br />
		<input class="text ui-widget-content ui-corner-all" type="text" name="title" id="title" value="{{data['title']}}" />
		%if 'title' in errors.keys():
			<br /><span class="error">{{errors['title']}}</span>
		%else:
			<br /><span class="error"></span>
		%end
	</p>
	<p class="field date">
		<label for="date">Date</label><br />
		<input class="date datepicker ui-widget-content ui-corner-all" type="text" name="date" id="date" value="{{data['date']}}" />
		%if 'date' in errors.keys():
			<br /><span class="error">{{errors['date']}}</span>
		%else:
			<br /><span class="error"></span>
		%end
	</p>
	<p class="field time">
		<label for="time">Time</label><br />
		<input class="time timepicker ui-widget-content ui-corner-all" type="text" name="time" id="time" value="{{data['time']}}" />
		%if 'time' in errors.keys():
			<br /><span class="error">{{errors['time']}}</span>
		%else:
			<br /><span class="error"></span>
		%end
	</p>
	<p class="field location">
		<label for="location">Location</label><br />
		<input class="text ui-widget-content ui-corner-all" type="text" name="location" id="location" value="{{data['location']}}" />
		%if 'location' in errors.keys():
			<br /><span class="error">{{errors['location']}}</span>
		%else:
			<br /><span class="error"></span>
		%end
	</p>
	<p class="field description">
		<label for="description">Description</label><br />
		<input class="text ui-widget-content ui-corner-all" type="text" name="description" id="description" value="{{data['description']}}" />
		%if 'description' in errors.keys():
			<br /><span class="error">{{errors['description']}}</span>
		%else:
			<br /><span class="error"></span>
		%end
	</p>
%if not get('ajax', False):
	<p class="field submit">
		<input class="ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only" type="submit" value="Edit" />
	</p>
%end_if
</form>
%if not get('ajax', False):
	%rebase forms title=title
%end