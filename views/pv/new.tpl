		<h1>SPVM</h1>
		<h2>New PV</h2>
		<div class="form clearfix">
			<form action="/pvs/new" method="post">
				<p class="field title">
					<label for="title">Title</label><br />
					<input type="text" name="title" id="title" />
					%if 'title' in errors.keys():
						<br /><span class="error">{{errors['title']}}</span>
					%else:
						<span class="error"></span>
					%end
				</p>
				<p class="field date">
					<label for="date">Date</label><br />
					<input type="text" name="date" id="date" class="date datepicker" />
					%if 'date' in errors.keys():
						<br /><span class="error">{{errors['date']}}</span>
					%else:
						<span class="error"></span>
					%end
				</p>
				<p class="field time">
					<label for="time">Time</label><br />
					<input type="text" name="time" id="time" class="time timepicker" />
					%if 'time' in errors.keys():
						<br /><span class="error">{{errors['time']}}</span>
					%else:
						<span class="error"></span>
					%end
				</p>
				<p class="field location">
					<label for="location">Location</label><br />
					<input type="text" name="location" id="location" />
					%if 'location' in errors.keys():
						<br /><span class="error">{{errors['location']}}</span>
					%else:
						<span class="error"></span>
					%end
				</p>
				<p class="field description">
					<label for="description">Description</label><br />
					<input type="text" name="description" id="description" />
					%if 'description' in errors.keys():
						<br /><span class="error">{{errors['description']}}</span>
					%else:
						<span class="error"></span>
					%end
				</p>
				<p class="field submit">
					<td colspan="3"><input type="submit" value="Create" />
				</p>
			</form>
		</div>
		%rebase layout title='New PV &mdash; SPVM'