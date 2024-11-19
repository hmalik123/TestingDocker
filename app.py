from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Define your SharePoint-like data structure here
class SpecialInterestGroup:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"SpecialInterestGroup({self.name})"

class Owner:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Owner({self.name})"

class Attachment:
    def __init__(self, file_url, description=""):
        self.file_url = file_url
        self.description = description

    def __repr__(self):
        return f"Attachment(URL: {self.file_url}, Description: {self.description})"

class IdeaPass:
    def __init__(self, status):
        self.status = status

    def __repr__(self):
        return f"IdeaPass({self.status})"

class Item:
    def __init__(self, ID, Date, Name, SpecialInterestGroup, Originator, Gate, Owner, Areas, 
                 IdeaPass, OnePager, Score, TimeToMarket, Impact, Attachment, Source, 
                 Description, Modified, Created, LegacyID, Thumbnail, ToBeRevised):
        self.ID = ID
        self.Date = Date
        self.Name = Name
        self.SpecialInterestGroup = SpecialInterestGroup
        self.Originator = Originator
        self.Gate = Gate
        self.Owner = Owner
        self.Areas = Areas
        self.IdeaPass = IdeaPass
        self.OnePager = OnePager
        self.Score = Score
        self.TimeToMarket = TimeToMarket
        self.Impact = Impact
        self.Attachment = Attachment
        self.Source = Source
        self.Description = Description
        self.Modified = Modified
        self.Created = Created
        self.LegacyID = LegacyID
        self.Thumbnail = Thumbnail
        self.ToBeRevised = ToBeRevised

    def to_dict(self):
        return {
            "ID": self.ID,
            "Date": self.Date,
            "Name": self.Name,
            "Special Interest Group": repr(self.SpecialInterestGroup),
            "Originator": self.Originator,
            "Gate": self.Gate,
            "Owner": repr(self.Owner),
            "Areas": self.Areas,
            "Idea Pass": repr(self.IdeaPass),
            "One Pager": self.OnePager,
            "Score": self.Score,
            "Time to Market": self.TimeToMarket,
            "Impact": self.Impact,
            "Attachment": repr(self.Attachment),
            "Source": self.Source,
            "Description": self.Description,
            "Modified": self.Modified,
            "Created": self.Created,
            "Legacy ID": self.LegacyID,
            "Thumbnail": self.Thumbnail,
            "To be Revised": self.ToBeRevised,
        }

class SharePointPage:
    def __init__(self, title):
        self.title = title
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def to_dict(self):
        return {
            "title": self.title,
            "items": [item.to_dict() for item in self.items]
        }

class SharePointSite:
    def __init__(self):
        self.pages = {}

    def add_page(self, page):
        self.pages[page.title] = page

    def to_dict(self):
        return {title: page.to_dict() for title, page in self.pages.items()}

# Set up a sample site with one page and one item
site = SharePointSite()
sample_page = SharePointPage("Sample Page")
sample_item = Item(
    ID=1,
    Date="2024-11-14",
    Name="Sample Item",
    SpecialInterestGroup=SpecialInterestGroup("Technology"),
    Originator="John Doe",
    Gate="G1",
    Owner=Owner("Jane Doe"),
    Areas="Area 51",
    IdeaPass=IdeaPass("Yes"),
    OnePager="Available",
    Score=8.5,
    TimeToMarket="6 months",
    Impact="High",
    Attachment=Attachment("link_to_file", "Sample attachment"),
    Source="Internal",
    Description="Sample description",
    Modified="2024-11-10",
    Created="2024-01-01",
    LegacyID=123,
    Thumbnail="link_to_thumbnail",
    ToBeRevised="No"
)
sample_page.add_item(sample_item)
site.add_page(sample_page)

# Define route to serve the HTML
@app.route('/')
def index():
    return render_template('index.html')

# Define route to return JSON data
@app.route('/data')
def get_data():
    return jsonify(site.to_dict())

# Add more routes for various functionality
@app.route('/items')
def get_items():
    return jsonify([item.to_dict() for page in site.pages.values() for item in page.items])

# Run the Flask app if the script is executed directly
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
