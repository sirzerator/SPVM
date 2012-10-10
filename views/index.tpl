		<h1>SPVM</h1>
		<h2>PVs</h2>
		<table>
			<thead>
				<th>#</th>
				<th>Titre</th>
				<th>Date</th>
				<th>Time</th>
				<th>Location</th>
				<th>Description</th>
				<th>Actions</th>
			</thead>
			<tbody>
			%if pvs['count']:
				%for id, user_id, title, date, time, location, description, code_id, lock_id, created, modified in pvs['rows']:
					<td>{{id}}</td>
					<td>{{title}}</td>
					<td>{{date}}</td>
					<td>{{time}}</td>
					<td>{{location}}</td>
					<td>{{description}}</td>
					<td><a href="/pvs/select/{{id}}">Select</a><br /><a href="/pvs/edit/{{id}}">Edit</a><br /><a href="/pvs/delete/{{id}}">Delete</a></td>
				%end
			%else:
				<td colspan="3">No PVs to display</td>
			%end
			</tbody>
		</table>
		<a href="/pvs/new" class="button">Add new PV</a>
		%rebase layout title='SPVM'