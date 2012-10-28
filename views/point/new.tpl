		<h1>SPVM</h1>
		<h2>New Point</h2>
		<div class="form clearfix">
			<form id="point_new" action="/point/new" method="post">
				<input type="hidden" id="pv_id" name="pv_id" value="{{pv_id}}" />
				<p class="field title">
					<label for="title">Title</label><br />
					<input class="text ui-widget-content ui-corner-all" type="text" name="title" id="title" />
					%if 'title' in errors.keys():
						<br /><span class="error">{{errors['title']}}</span>
					%else:
						<span class="error"></span>
					%end
				</p>
				<p class="field description">
					<label for="description">Description</label><br />
					<input class="text ui-widget-content ui-corner-all" type="text" name="description" id="description" />
					%if 'description' in errors.keys():
						<br /><span class="error">{{errors['description']}}</span>
					%else:
						<span class="error"></span>
					%end
				</p>
				<p class="field rank">
					<label for="rank">Rank</label><br />
					<input class="text ui-widget-content ui-corner-all" type="text" name="rank" id="rank" />
					%if 'rank' in errors.keys():
						<br /><span class="error">{{errors['rank']}}</span>
					%else:
						<span class="error"></span>
					%end
				</p>
				<p class="field parent">
					<label for="parent_id">Parent</label><br />
					<select id="parent_id" name="parent_id">
						<option value="0">---</option>
						%if points['count']:
							%for point in points['rows']:
								<option value="{{point['id']}}">{{point['title']}}</option>
							%end
						%end
					</select>
				</p>
				<p class="field submit">
					<input class="ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only" type="submit" value="Create" />
				</p>
			</form>
		</div>
		<script type="text/javascript">
			reassignUiElements();
			assignButtonElements($('.form.clearfix'));
		</script>
		%rebase layout title='New PV &mdash; SPVM'