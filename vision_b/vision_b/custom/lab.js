frappe.ui.form.on('Lab Test', {
    fetch: function(frm){
		frappe.call({
			method: 'vision_b.vision_b.custom.lab.xml_file_upload',
			args: { doc: frm.doc.upload },
			callback: function (r) {
				cur_frm.set_value("compound_test_result", r.message)
			}
		});
	}
	
});