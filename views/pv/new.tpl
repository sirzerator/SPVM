		<h1>SPVM</h1>
		<h2>New PV</h2>
		<form action="/pvs/new" method="post">
			<div>
				<p>
					<label for="title">Title</label>
					<input type="text" name="title" id="title" />
					%if 'title' in errors.keys():
						<br />{{errors['title']}}
					%end
				</p>
				<p>
					<label for="date">Date</label>
					<input type="text" name="date" id="date" class="datepicker" />
				</p>
				<p>
					<label for="time">Time</label>
					<input type="text" name="time" id="time" class="timepicker" />
				</p>
				<p>
					<label for="location">Location</label>
					<input type="text" name="location" id="location" />
				</p>
				<p>
					<label for="description">Description</label>
					<input type="text" name="description" id="description" />
				</p>
				<p>
					<td colspan="3"><input type="submit" value="Create" />
				</p>
			</div>
		</form>
		%rebase layout title='New PV &mdash; SPVM'