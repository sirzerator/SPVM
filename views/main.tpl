		<h1>SPVM</h1>
		<div class="controls">
			<span class="configuration"></span>
			<span class="quit"><a href="/pv/close">Close</a></span>
		</div>
		<h2>{{pv_data['title']}}</h2>
		<div class="informations toggle">
			<div class="location">{{pv_data['location']}}</div>
			<div class="date time">{{pv_data['date']}} {{pv_data['time']}}</div>
			<div class="description">{{pv_data['description']}}</div>
			<div class="modified">{{pv_data['modified']}}</div>
		</div>
		<div class="points left">
			<p class="buttons"><a href="/point/new" class="button new point"><button class="ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only"><span class="ui-button-text">New Point</span></button></a></p>
			%if points['count']:
				%counters = [0]
				%level = 0
				%for point in points['rows']:
					<div class="point level{{level}}">
						<span class="number">
						%number = ""
						%for r in range(level+1):
							%number += str(counters[r]+1) + "."
						%end
						{{number}}
						</span>
						&nbsp;
						<span class="title">{{point['title']}}</span>
						%if point['description']:
							&mdash; <span class="description">{{point['description']}}</span>
						%end
					</div>
					%counters[level] += 1
				%end
			%else:
				<div class="ajax point">
					<span class="number">1.</span>
					<input class="title placeholder" value="Click here to add a new point" />
				</div>
				<div class="overflow point">
					<span class="number">1.</span>

				</div>
			%end
		</div>
		%rebase layout title='SPVM'