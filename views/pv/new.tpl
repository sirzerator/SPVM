		<h1>SPVM</h1>
		<h2>New PV</h2>
		<div class="form clearfix">
			<form action="/pvs/new" method="post">
				<p>
					<label for="title">Title</label><br />
					<input type="text" name="title" id="title" />
					%if 'title' in errors.keys():
						<br />{{errors['title']}}
					%end
				</p>
				<p>
					<label for="date">Date</label><br />
					<input type="text" name="date" id="date" class="date datepicker" />
					%if 'date' in errors.keys():
						<br />{{errors['title']}}
					%end
				</p>
				<p>
					<label for="time">Time</label><br />
					<input type="text" name="time" id="time" class="time timepicker" />
					%if 'time' in errors.keys():
						<br />{{errors['title']}}
					%end
				</p>
				<p>
					<label for="location">Location</label><br />
					<input type="text" name="location" id="location" />
					%if 'location' in errors.keys():
						<br />{{errors['title']}}
					%end
				</p>
				<p>
					<label for="description">Description</label><br />
					<input type="text" name="description" id="description" />
					%if 'description' in errors.keys():
						<br />{{errors['title']}}
					%end
				</p>
				<p>
					<td colspan="3"><input type="submit" value="Create" />
				</p>
			</form>
		</div>
		%rebase layout title='New PV &mdash; SPVM'