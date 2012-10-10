		<h1>SPVM</h1>
		<h2>New PV</h2>
		<form action="/pvs/new" method="post">
			<table>
				<tr>
					<td><label for="title">Title</label></td>
					<td><input type="text" name="title" id="title" />
					%if 'title' in errors.keys():
						<br />{{errors['title']}}
					%end
					</td>
				</tr>
				<tr>
					<td><label for="date">Date</label></td>
					<td><input type="text" name="date" id="date" /></td>
				</tr>
				<tr>
					<td><label for="time">Time</label></td>
					<td><input type="text" name="time" id="time" /></td>
				</tr>
				<tr>
					<td><label for="location">Location</label></td>
					<td><input type="text" name="location" id="location" /></td>
				</tr>
				<tr>
					<td><label for="description">Description</label></td>
					<td><input type="text" name="description" id="description" /></td>
				</tr>
				<tr>
					<td colspan="3"><input type="submit" value="Create" /></td>
		</form>
		</form>
		%rebase layout title='New PV &mdash; SPVM'