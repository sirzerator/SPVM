<p><span class="ui-icon ui-icon-alert" style="float: left; margin: 5px 7px 5px 0;"></span>This participant and all related items will be permanently deleted and cannot be recovered.</p>
<form id="participant_delete" action="/participant/delete" method="post">
	<input type="hidden" value="{{participant_id}}" id="participant_id" name="participant_id" />
%if not get('ajax', False):
	<p class="field submit">
		<input id="yes" name="yes" type="submit" value="Yes" />
		<input id="no" name="no" type="submit" value="No" />
	</p>
%end
</form>
%if not get('ajax', False):
	%rebase forms title=title
%end