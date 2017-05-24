class Team:
	def __init__(self, name, location, conference, division, championships, appearances, y_start):
		self.name = name
		self.location = location
		self.conference = conference
		self.division = division
		self.championships = championships
		self.appearances = appearances
		self.y_start = y_start

BOS_Celtics = Team('Boston Celtics', 'Boston', 'Eastern', 'Atlantic', 17, 21, 1946)
BRK_Nets = Team('Nets', 'Brooklyn', 'Eastern', 'Atlantic', 0, 2, 1967)
NY_Knicks = Team('Knicks', 'New York', 'Eastern', 'Atlantic', 2, 8, 1946)
PHI_76ers = Team('76ers', 'Philadelphia', 'Eastern', 'Atlantic', 3, 9, 1946)
TOR_Raptors = Team('Raptors', 'Toronto', 'Eastern', 'Atlantic', 0, 0, 1995)

CHI_Bulls = Team('Chicago Bulls', 'Bulls', 'Chicago', 'Eastern', 'Central', 6, 6, 1966)
CLE_Cavaliers = Team('Cavaliers', 'Cleveland', 'Eastern', 'Central', 1, 3, 1970)
DET_Pistons = Team('Pistons', 'Detroit', 'Eastern', 'Central', 3, 7, 1941)
IND_Pacers = Team('Pacers', 'Indiana', 'Eastern', 'Central', 0, 1, 1967)
MIL_Bucks = Team('Bucks', 'Milwaukee', 'Eastern', 'Central', 1, 2, 1968)

ATL_Hawks = Team('Hawks', 'Atlanta', 'Eastern', 'Southeast', 1, 4, 1946)
CHA_Hornets = Team('Hornets', 'Charlotte', 'Eastern', 'Southeast', 0, 0, 1988)
MIA_Heat = Team('Heat', 'Miami', 'Eastern', 'Southeast', 3, 5, 1988)
ORL_Magic = Team('Magic', 'Orlando', 'Eastern', 'Southeast', 0, 2, 1989)
WSH_Wizards = Team('Wizards', 'Washington, D.C.', 'Eastern', 'Southeast', 1, 3, 1961)

GS_Warriors = Team('Warriors', 'Oakland', 'Western', 'Pacific', 4, 8, 1946)
LA_Clippers = Team('Clippers', 'Los Angeles', 'Western', 'Pacific', 0, 0, 1970)
LA_Lakers = Team('Los Angeles Lakers', 'Los Angeles', 'Western', 'Pacific', 16, 31, 1947)
PHO_Suns = Team('Suns', 'Phoenix', 'Western', 'Pacific', 0, 2, 1968)
SAC_Kings = Team('Kings', 'Sacramento', 'Western', 'Pacific', 1, 1, 1948)

DAL_Mavericks = Team('Mavericks', 'Dallas', 'Western', 'Southwest', 1, 2, 1980)
HOU_Rockets = Team('Rockets', 'Houston', 'Western', 'Southwest', 2, 4, 1967)
MEM_Grizzlies = Team('Grizzlies', 'Memphis', 'Western', 'Southwest', 0, 0, 1995)
NO_Pelicans = Team('Pelicans', 'New Orleans', 'Western', 'Southwest', 0, 0, 2002)
SA_Spurs = Team('Spurs', 'San Antonio', 'Western', 'Southwest', 5, 6, 1967)

DEN_Nuggets = Team('Nuggets', 'Denver', 'Western', 'Northwest', 0, 0, 1967)
MIN_Timberwolves = Team('Timberwolves', 'Minnesota', 'Western', 'Northwest', 0, 0, 1989)
OKC_Thunder = Team('Thunder', 'Oklahoma City', 'Western', 'Northwest', 1, 4, 1967)
POR_TrailBlazers = Team('Trail Blazers', 'Portland', 'Western', 'Northwest', 1, 3, 1970)
UTA_Jazz = Team('Jazz', 'Salt Lake City', 'Western', 'Northwest', 0, 2, 1974)

class Player:
	def __init__(self, name, Team, number, position, height, weight, span)
		self.name = name
		self.Team = Team
		self.number = number
		self.position = position
		self.height = height
		self.weight = weight
		self.span = span

