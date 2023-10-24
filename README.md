# file_transfer_client
<summary> <b>BACKGROUND:</b> created this program for my dad over 3 nights while I was visiting him. He is not tech savy and needed help trasfering his music from his PC -> android phone. Created a Batch file to automate it for him afterwards.</summary>

<h1> WHAT IS DOES</h1>
Once ran it will download(transfer) all files with specified extension and checking if file exist in order to not overwrite and waste time/resources.

<h1>HOW IT'S MENT TO BE RUN(transfering from pc to android)</h1>
<p>
  <b>REQUIREMENTS:</b> <br>1.python3 installed on server machine. <br> 2.pydroid 3 application installed on android.
<br><br>
  <h3>PC STEPS</h3>
  <step1><b>STEP1: </b>open cmd or powershell and navigate to folder you will be sharing files from.</step1><br>
  <step2><b>STEP2:</b> </step2> On  PC create an http server with pythons function. I like to specify my ip address from which network adapter I will be using but not required.<br>
  <p ><i>example:</i> >python -m http.server --bind 192.168.1.148 8000</p>(replace IP ADDRESS with your LAN ip address.)<br><br>

  <h3>android steps</h3>
  <step1><b>STEP1: </b> Download this github script on android and open with pydroid 3</step1><br>
  <step2><b>STEP2: </b> Adjust preset variables.(theURL, saveSpot, fileType)</step2><br>
  <step3><b>STEP3: </b> run script</step3>
  
</p>

<h1>RECOMMENDED</h1>
<p>
  create a batch file to automate the python http server(pc side). Doing so will lead to a simplistic efficient reliable transfers.
</p>
