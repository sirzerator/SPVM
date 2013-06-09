<div class="participation">
	<h2>Participants</h2>
	<div class="buttons"><form method="GET" action="/participant/new">
		<button class="new participant ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only"><!--<a href="/participant/new">--><span class="ui-button-text">New Participant</span><!--</a>--></button>
		<input type="hidden" id="pv_id" name="pv_id" value="{{pv_id}}" />
	</form></div>

	<div class="participants">
	%if participants['count']:
		%for participant in participants['rows']:
		<div class="participant" id="participant_{{participant['id']}}"><p class="text"><span class="full_name">{{participant['full_name']}}</span></p>
			<ul class="icons ui-widget ui-helper-clearfix">
				<li class="ui-state-default ui-corner-all"><a href="/participant/edit/{{participant['id']}}" class="participant edit" data-rel="{{participant['id']}}" title="Edit"><span class="ui-icon ui-icon-pencil"></span></a></li>
				<li class="ui-state-default ui-corner-all"><a href="/participant/delete/{{participant['id']}}" class="participant delete" data-rel="{{participant['id']}}" title="Delete"><span class="ui-icon ui-icon-trash"></span></a></li>
			</ul>
		</div>
		%end
	%end
		<div class="participant overflow" id="participant_*|id|*"><p class="text"><span class="full_name">*|full_name|*</span></p>
			<ul class="icons ui-widget ui-helper-clearfix">
				<li class="ui-state-default ui-corner-all"><a href="/participant/edit/*|id|*" class="participant edit" data-rel="*|id|*" title="Edit"><span class="ui-icon ui-icon-pencil"></span></a></li>
				<li class="ui-state-default ui-corner-all"><a href="/participant/delete/*|id|*" class="participant delete" data-rel="*|id|*" title="Delete"><span class="ui-icon ui-icon-trash"></span></a></li>
			</ul>
		</div>
	</div>
	%if not participants['count']:
	<div class="nothing participant">
		<span>No participant.</span>
	</div>
	%end
</div>
<script type="text/javascript">
	$(document).ready(function() {
		$(".participant.new").click(function(e) {
			e.preventDefault();
			properties = {
				title:"New participant",
				OK:"Add",
				Cancel:"Cancel",
				width:200,
				height:150,
				modal:true,
				resizable:false
			}
			castDialog('participant', 'new', properties, null);
		});
		$(".participants").delegate(".participant.edit", "click", function(e) {
			e.preventDefault();
			properties = {
				title:"Edit Participant",
				OK:"Edit",
				Cancel:"Cancel",
				width:200,
				height:150,
				modal:true,
				resizable:false
			}
			castDialog('participant', 'edit', properties, "participant_id=" + $(this).attr('data-rel'));
		});
		$(".participants").delegate(".participant.delete", "click", function(e) {
			e.preventDefault();
			properties = {
				title:"Are you sure you want to delete this participant ?",
				OK:"Yes",
				Cancel:"No",
				width:320,
				height:140,
				modal:true,
				resizable:false
			}
			castDialog('participant', 'delete', properties, "participant_id=" + $(this).attr('data-rel'));
		});
	});
</script>