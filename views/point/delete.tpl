<p><span class="ui-icon ui-icon-alert" style="float: left; margin: 5px 7px 5px 0;"></span>This point and all sub-points will be permanently deleted and cannot be recovered.</p>
<form id="point_delete" action="/point/delete" method="post">
	<input type="hidden" value="{{point_id}}" id="point_id" name="point_id" />
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