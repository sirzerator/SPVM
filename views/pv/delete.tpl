	<h1>SPVM</h1>
	<h2>Delete PV</h2>
	<div class="form clearfix">
		<p><span class="ui-icon ui-icon-alert" style="float: left; margin: 5px 7px 5px 0;"></span>These items will be permanently deleted and cannot be recovered. Are you sure ?</p>
		<form id="pv_delete" action="/pv/delete" method="post">
			<input type="hidden" value="{{pv_id}}" id="pv_id" name="pv_id" />
			<p class="field submit">
				<input type="submit" value="Yes" />
				<input type="submit" value="No" />
			</p>
		</form>
	</div>
	<script type="text/javascript">
		reassignUiElements();
		assignButtonElements($('.form.clearfix'));
	</script>
	%rebase layout title='Delete PV &mdash; SPVM'