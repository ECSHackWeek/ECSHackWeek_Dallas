echo "Creating RDE directory"
mkdir RDE

echo "Changing into RDE directory"
cd RDE

echo "Creating README.txt"
echo "This is Trevor's Rotating Disc Electrode data" > README.txt
echo "100mv data" >> README.txt

echo "Downloading RDE data and saving to rde.csv"
curl -o rde.csv "https://files.osf.io/v1/resources/qrhcw/providers/osfstorage/59ceb2079ad5a102cd5c41bb?action=download&amp;version=1&amp;direct"

echo "Showing the first 10 lines of rde.csv"
head rde.csv
