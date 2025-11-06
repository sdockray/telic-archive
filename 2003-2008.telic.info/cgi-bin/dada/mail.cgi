<!--?xml version="1.0"?--><!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml"><head>
  <!-- TELIC Arts Exchange 2.10.16 --> 
  <title>Sign Up for a List</title>
  <style type="text/css" media="all">
   <!--
   /* Not @imported, since AOL rejects msgs with linked stylesheets 
      (see: http://www.alistapart.com/articles/cssemail/ )
   */
   
/* ----- GENERAL ----- */

body { 
	background-color:#fff;
	font-family:Georgia,Times,'Times New Roman',serif;
	font-size:13px;
	line-height:150%;
}

/* for list/archive pages only: */
body#Dada {
	margin:50px 0;
	padding:0;
	text-align:center;                /* page centering hack for IE */
	
}

/* for admin pages only: */
body#DadaAdmin {
	margin:0;
	padding:0;
}

/* ----- IDS: General Page Layout ----- */

#PageWrapper {
}

#Header {
	width:550px;
	margin:0 auto;                    /* page centering for all but IE */
	padding:20px;
	padding-bottom:10px;
	border:1px solid #000;
	background-color:#c66;
	text-align:left;                  /* overrides page centering hack for IE (in the body) */
	font-family:AvantGarde,'Avant Garde',Verdana,Arial,sans-serif;
	font-size:18px;
	font-style:italic;
	font-weight:bold;
	text-transform:uppercase;
	color:#000;
}

/* box model hack for IE: \*/
* html #Header {
	width:592px;
}
/* ends the box model hack. see: http://tinyurl.com/9yld6 */

/* override for admin pages only: */
body#DadaAdmin #Header {
	width:auto;
}

/* override for admin pages only: */
/* box model hack for IE: \*/
* html body#DadaAdmin #Header {
	width:100%;
}
/* ends the box model hack. see: http://tinyurl.com/9yld6 */

#Logo {
	float:left;
	text-align:left;
}

#Title {
	float:right;
	text-align:right;
}

/* alas, IE doesn't understand the next three CSS2 rules, 
   which add the dots before and after the header copy: */
#Logo:before {
	content: ".: ";
}

#Title:before {
	content: ":: ";
}

#Title:after {
	content: " ::";
}

#Content {
	width:550px;
	margin:0 auto;                    /* page centering for all but IE */
	padding:20px;
	border:1px solid #000;
	border-top:0;
	background-color:#fff;
	text-align:left;                  /* overrides page centering hack for IE (in the body) */
}

/* box model hack for IE: \*/
* html #Content {
	width:592px;
}
/* ends the box model hack. see: http://tinyurl.com/9yld6 */

#AdminPageWrapper {
}

#AdminContentWrapper {
	margin:0 0 50px 200px;
	padding:10px 50px;
}

#AdminContent {
	width:100%;
	padding-top:8px;
}

#MenuWrapper {
}

#Menu {
	position:absolute;
	top:70px;
	left:20px;
	width:160px;
	padding:1px 10px 0 10px;
	border:1px solid #000;
	background-color:#fff;
	text-align:left;
	line-height:150%;
}

/* box model hack for IE: \*/
* html #Menu {
	width:182px;
} 
/* ends the box model hack. see: http://tinyurl.com/9yld6 */

/* ----- IDS: Navigation ----- */

#Menu li {
	line-height:125%;
}

#Menu p, 
#Menu ul
{
	margin-left: 0px;
	padding-left: 0px;
	list-style: none;
	font-family: AvantGarde,'Avant Garde',Verdana,Arial,sans-serif;
	font-size: 12px;
	font-weight: bold;
}

#Menu ul ul {
	padding-left:12px;
	font-weight:normal;
    list-style-type: square;
    color: #ccc;
}

#list_type_switcher div { 
	float:left;
	margin-right:2px;
	width:150px;
	border:1px solid #000;
	background-color:#ccc;
	text-align:center;
}

#list_type_switcher div a, 
#list_type_switcher div span {
	padding:8px 0;
	                                  /* these next two make the entire "button" clickable: */
	display:block; /* Moz, etc. */
	width:150px;   /* IE */
}

#list_type_switcher div span {
	background-color:#fff;
	font-weight:bold;
}

#list_type_switcher div a:hover {
	background-color: #fcc;	
}

/* ----- IDS: Widgets/Other ----- */

#breadcrumbs {
}

#help_link {
	float:right;
	margin-top:2em;
	font-weight:bold;
	clear:both;
}

#root_login_message {
	float:right;
	margin-right:0.5em;
	color:#fff;
}

/* ----- CLASSES ----- */

.disabled {
	background-color:#ccc;
	border:1px solid #fff;
}

.error {
	font-family:Verdana,Arial,sans-serif;
	font-size:11px;
	font-style:italic;
	color:#600;
}

.hidden {
	display:none;
}

.greyed_out { 
    color: #ccc;
    font-style:italic;
}

.highlighted { 
    font-style: normal;
    background-color:#6F3;

}

p.link_to_screen {
	text-align:right;
	font-weight:bold;
}

.positive {
	font-family:Verdana,Arial,sans-serif;
	font-size:11px;
	color:#063;
}

.simplebox {
	padding:7px;
	border:1px solid #000;
	background-color:#fff;
}

.login_message { 
    float: right; 
    padding:5px;
    /* width:150px; */
    background-color:#ff9;
    border:1px dotted #333;
}

.login_message p { 
    line-height: 100%;
}

.login_message ul { 

    list-style-type: square;
    color: #ccc;
    
}


/* all but IE/Win & NN4: */
.simplebox>p {
	margin:0;
}

/* ----- HEADINGS ----- */

h1, h2, h3 {
	font-family:AvantGarde,'Avant Garde',Arial,sans-serif;
	font-weight:bold;
}

h1 {
	font-size:18px;
}

h2 {
	font-size:16px;
}

h3 {
	font-size:14px;
}

/* ----- PARAGRAPHS ----- */

p {
}

p.small {
	font-family:Verdana,Arial,sans-serif;
	font-size:11px;
}

/* ----- CODE ----- */

code, pre {
	margin:3px;
	padding:3px;
	border:1px dotted #000;
	background-color:#ccf;
	font:9px/14px Monaco,Mono,'Courier New',Courier,monospace;
}

/* ----- LINKS ----- */

a {
	text-decoration:none;
}

a:link {
	color:#339;
}

a:visited {
	color:#03c;
}

a:hover {
	color:#33c;
}

a:active {
}

#Logo a:link, 
#Logo a:visited {
	color:#000;
}

#Logo a:hover {
	color:#000;
}

#Logo a:active {
}

/* ----- FORMS ----- */

label {
	font-family:AvantGarde,'Avant Garde',Verdana,Arial,sans-serif;
	font-size:12px;
	font-weight:bold;
	color:#000;
}

fieldset { 

    border: 1px solid black;
    
}


legend {
	font-family:AvantGarde,'Avant Garde',Arial,sans-serif;
	font-weight:bold;
    font-size:16px;

}




input {
	margin:3px;
	padding:3px;
	border-width:1px;
	border-style:solid;
	border-color:#000 #999 #999 #000;
	font-family:Verdana,Arial,sans-serif;
	font-size:12px;
	color:#333;
}

/* removes checkbox/radio-button borders in IE 5.0+: */
/* (commented out for validation, uncomment to apply)
input {
    border: expression(this.type=="checkbox"? 'none':
                       this.type=="radio"?    'none':
                       '1px solid #000');
}
*/

input.full {
	width:95%;
}

select {
	margin:3px;
	font-family:Verdana,Arial,sans-serif;
	font-size:12px;
	color:#333;
}

textarea {
	padding:10px;
	width:95%;
	border-width:1px;
	border-style:solid;
	border-color:#000 #999 #999 #000;
	font-family:Verdana,Arial,sans-serif;
	font-size:12px;
	color:#333;
}

/* affects buttons only: */
input.plain,
input.processing,
input.cautionary,
input.alertive {
	font-weight:bold;
	color:#000;
}

input.plain {
	background-color:#ccf;
}

input.processing {
	background-color:#9c9;
}

input.cautionary {
	background-color:#ffc;
}

input.alertive {
	background-color:#f66;
}

/* IE doesn't understand this: */
input:focus, 
textarea:focus {
	border-color:#009 #33c #33c #009;
}

div.buttonfloat {
	float:right;
}

/* ----- TABLES ----- */

table {
	font-size:100%;                   /* fixes IE inheritance bug, redundant for others */
}

td {
	vertical-align:top;
}

/* all but IE/Win & NN4: */
td>p {
	margin:0;
}

table.tagchart {
	border-collapse:collapse;
	border:2px solid #000;
	background-color:#fff;
	width:100%;
}

table.tagchart td {
	border:1px solid #000;
	padding:5px;
}

/* ----- BREAKS ----- */

hr {
	width:66%;
	text-align:center;
	height:1px;
	border:0;
	color:#000;                       /* IE */
	background-color:#000;            /* Moz & Opera */
	clear:both;
}

div.floatclear {
	clear:both;
	height:1px;
	overflow:hidden;
}

/* ----- ARCHIVES ----- */

#archived_message_wrapper {
}

#archived_message_head {
}

iframe#archived_message_body_container {
	height:500px;
	width:100%;
	border:1px solid #000;
	/* text-styling rules will have NO effect in here. see below instead. */
}

#archived_message_body {
/* inline-displayed HTML messages keep their inline styles, but can otherwise be styled here.
   iframe-displayed HTML messages *always* retain their own style. this does nothing for 'em.
   plain text messages, whether inline or iframed, will be styled here also. */
}

.quoted_reply { 
	color:#666;
	font-style:italic;
}

#archived_attachments_wrapper {
}


 ul.archive_badges_ul{ font-size:  11px;
line-height: 13px; }

li.archive_badges_li {
display: inline;
padding-left: 3px;
padding-right: 7px;
/* border-right: 1px dotted #066; */
}




   -->
  </style>
 </head>
 
 <body id="Dada">
  <div id="PageWrapper">
   
   <div id="Header">
    <span id="Logo">
     <a href="http://www.telic.info/cgi-bin/dada/mail.cgi">TELIC Arts Exchange</a>
    </span>
    <span id="Title">
     Sign Up for a List
    </span>
    <div class="floatclear"></div>
   </div><!-- ends id="Header" -->
   
   <div id="Content">
    <!-- begin default_screen.tmpl -->




 

    <!-- begin list_popup_subscription_form.tmpl -->

<form action="http://www.telic.info/cgi-bin/dada/mail.cgi" method="post">
 <table cellpadding="5" cellspacing="0">
  <tbody><tr>
   <td width="300">
    <p>
     Choose a 
     <label for="list">
      list</label>:
    </p>
   </td>
   <td width="300" align="right">
    <p>
     Enter your 
     <label for="email">
      email 
     </label>
     address:
    </p>
   </td>
  </tr>
  <tr>
   <td valign="top">
    <select name="list" style="width:200px" id="list">
<option value="announcements">TELIC</option>
</select>
   </td>
   <td valign="top" align="right">
    <input type="text" name="email" id="email" size="20" value="" maxlength="1024">
   </td>
  </tr>
  <tr>
   <td valign="top">
    <p>
     

	     
	     <input type="radio" name="f" value="subscribe" id="subscribe" style="background-color:transparent" checked="checked">
	     <label for="subscribe">Subscribe</label> | 
	     <input type="radio" name="f" value="u" id="u" style="background-color:transparent">
	     <label for="u">Unsubscribe</label>
	     

     
    </p>
   </td>
   <td valign="top">
    <div class="buttonfloat">
     <input type="submit" value="Submit" class="processing">
    </div>
    <div class="floatclear"></div>
   </td>
  </tr>
 </tbody></table>
</form>

<!-- end list_popup_subscription_form.tmpl -->

    <h1>
     Available Lists:
    </h1>
    
    
        
        <h2>
         <a href="http://www.telic.info/cgi-bin/dada/mail.cgi/list/announcements/">
          TELIC
         </a>
        </h2>
        <p>
         </p><p>Announcements for TELIC Arts Exchange events -<br>
<br>
TELIC Arts Exchange is a platform for events and discussion.<br>
With an emphasis on social exchange, interactivity, and public participation, <br>
we set out to produce a critical engagement with new media and culture.<br>
<br>
TELIC Arts Exchange is a 501(c)3 non-profit organization.  </p>
        <p></p>
        
        
            
            
                
                <!-- TODO: replace this here blockquote with CSS -->
                <blockquote>
                 <p>
                  <strong>
                   <a href="http://www.telic.info/cgi-bin/dada/mail.cgi/archive/announcements/newest/">
                    Last Message: Julie Ault - Friday, December 10 at 8pm
                   </a>
                  </strong>
                 </p>
                 <p>
                  <em>
                   
body .everything { width: 650px; font-weight: normal; font-size : 11px; font-family: Verdana,
Arial,
Helvetica, sans-serif; }
.everything a { color: #333333; text-decoration: underline; }
.everything h3.title a {font-weight: bold; font-size: 12px; color: ...
                  </em>
                 </p>
                 <p style="text-align:right">
                  <a href="http://www.telic.info/cgi-bin/dada/mail.cgi/archive/announcements/newest/">
                   More...
                  </a>
                 </p>
                </blockquote>
                
            
        
        
    
    

 


	
	<p style="text-align:center">
	 <strong>
	  <a href="http://www.telic.info/cgi-bin/dada/mail.cgi/admin/">
	   Administration
	  </a>
	 </strong>
	</p>
	


<!-- end default_screen.tmpl -->
                                                                                                                                                                                                        <a href="http://www.telic.info/cgi-bin/dada/mail.cgi/art" style="font-size:1px;color:#FFFFFF">i &lt;3 u </a>
   </div><!-- ends id="Content" -->
   
  </div><!-- ends id="PageWrapper" -->
 
 

</body></html>