<form id="participant_new" action="/participant/new" method="post">
	<input type="hidden" id="pv_id" name="pv_id" value="{{pv_id}}" />
	<input type="hidden" id="group_id" name="group_id" value="0" />
	<p class="field full_name">
		<label for="full_name">Full name</label><br />
		<input class="text ui-widget-content ui-corner-all" type="text" name="full_name" id="full_name" />
		%if 'full_name' in errors.keys():
			<br /><span class="error">{{errors['full_name']}}</span>
		%else:
			<br /><span class="error"></span>
		%end
	</p>
%if not get('ajax', False):
	<p class="field submit">
		<input class="ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only" type="submit" value="Create" />
	</p>
%end_if
</form>
%if not get('ajax', False):
	%rebase forms title=title
%end_if