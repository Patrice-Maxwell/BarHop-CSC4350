(function(a){var b={isRTL:!1,defaults:{recordtext:"Pregled {0} - {1} od {2}",emptyrecords:"Nema zapisa",loadtext:"U\u010ditavam...",pgtext:"Stranica {0} od {1}",pgfirst:"First Page",pglast:"Last Page",pgnext:"Next Page",pgprev:"Previous Page",pgrecs:"Records per Page",showhide:"Toggle Expand Collapse Grid",savetext:"Spremanje..."},search:{caption:"Tra\u017ei...",Find:"Pretra\u017eivanje",Reset:"Poni\u0161ti",odata:[{oper:"eq",text:"jednak"},{oper:"ne",text:"nije identi\u010dan"},{oper:"lt",text:"manje"},
{oper:"le",text:"manje ili identi\u010dno"},{oper:"gt",text:"ve\u0107e"},{oper:"ge",text:"ve\u0107e ili identi\u010dno"},{oper:"bw",text:"po\u010dinje sa"},{oper:"bn",text:"ne po\u010dinje sa "},{oper:"in",text:"je u"},{oper:"ni",text:"nije u"},{oper:"ew",text:"zavr\u0161ava sa"},{oper:"en",text:"ne zavr\u0161ava sa"},{oper:"cn",text:"sadr\u017ei"},{oper:"nc",text:"ne sadr\u017ei"},{oper:"nu",text:"is null"},{oper:"nn",text:"is not null"}],groupOps:[{op:"I",text:"sve"},{op:"ILI",text:"bilo koji"}],
operandTitle:"Click to select search operation.",resetTitle:"Reset Search Value"},edit:{addCaption:"Dodaj zapis",editCaption:"Promijeni zapis",bSubmit:"Preuzmi",bCancel:"Odustani",bClose:"Zatvri",saveData:"Podaci su promijenjeni! Preuzmi promijene?",bYes:"Da",bNo:"Ne",bExit:"Odustani",msg:{required:"Polje je obavezno",number:"Molim, unesite ispravan broj",minValue:"Vrijednost mora biti ve\u0107a ili identi\u010dna ",maxValue:"Vrijednost mora biti manja ili identi\u010dna",email:"neispravan e-mail",
integer:"Molim, unjeti ispravan cijeli broj (integer)",date:"Molim, unjeti ispravan datum ",url:"neispravan URL. Prefiks je obavezan ('http://' or 'https://')",nodefined:" nije definiran!",novalue:" zahtjevan podatak je obavezan!",customarray:"Opcionalna funkcija trebala bi bili polje (array)!",customfcheck:"Custom function should be present in case of custom checking!"}},view:{caption:"Otvori zapis",bClose:"Zatvori"},del:{caption:"Obri\u0161i",msg:"Obri\u0161i ozna\u010den zapis ili vi\u0161e njih?",
bSubmit:"Obri\u0161i",bCancel:"Odustani"},nav:{edittext:"",edittitle:"Promijeni obilje\u017eeni red",addtext:"",addtitle:"Dodaj novi red",deltext:"",deltitle:"Obri\u0161i obilje\u017eeni red",searchtext:"",searchtitle:"Potra\u017ei zapise",refreshtext:"",refreshtitle:"Ponovo preuzmi podatke",alertcap:"Upozorenje",alerttext:"Molim, odaberi red",viewtext:"",viewtitle:"Pregled obilje\u017eenog reda"},col:{caption:"Obilje\u017ei kolonu",bSubmit:"Uredu",bCancel:"Odustani"},errors:{errcap:"Gre\u0161ka",
nourl:"Nedostaje URL",norecords:"Bez zapisa za obradu",model:"colNames i colModel imaju razli\u010ditu duljinu!"},formatter:{integer:{thousandsSeparator:".",defaultValue:"0"},number:{decimalSeparator:",",thousandsSeparator:".",decimalPlaces:2,defaultValue:"0,00"},currency:{decimalSeparator:",",thousandsSeparator:".",decimalPlaces:2,prefix:"",suffix:"",defaultValue:"0,00"},date:{dayNames:"Ned Pon Uto Sri \u010cet Pet Sub Nedjelja Ponedjeljak Utorak Srijeda \u010cetvrtak Petak Subota".split(" "),monthNames:"Sij Velj O\u017eu Tra Svi Lip Srp Kol Ruj Lis Stu Pro Sije\u010danj Velja\u010da O\u017eujak Travanj Svibanj Lipanj Srpanj Kolovoz Rujan Listopad Studeni Prosinac".split(" "),
AmPm:["am","pm","AM","PM"],S:function(){return""},srcformat:"Y-m-d",newformat:"d.m.Y.",masks:{ShortDate:"d.m.Y.",LongDate:"l, j. F Y",FullDateTime:"l, j. F Y H:i:s",MonthDay:"d F",ShortTime:"H:i",LongTime:"H:i:s",YearMonth:"F Y"}}}};a.jgrid=a.jgrid||{};a.extend(!0,a.jgrid,{defaults:{locale:"hr"},locales:{hr:a.extend({},b,{name:"hrvatski",nameEnglish:"Croatian"}),"hr-HR":a.extend({},b,{name:"hrvatski (Hrvatska)",nameEnglish:"Croatian (Croatia)"})}})})(jQuery);
