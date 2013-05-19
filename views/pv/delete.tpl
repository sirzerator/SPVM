<p><span class="ui-icon ui-icon-alert" style="float: left; margin: 5px 7px 5px 0;"></span>This PV and all related items will be permanently deleted and cannot be recovered.</p>
<form id="pv_delete" action="/pv/delete" method="post">
	<input type="hidden" value="{{pv_id}}" id="pv_id" name="pv_id" />
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