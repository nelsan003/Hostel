import { registry } from "@web/core/registry";
import { Component, onMounted , onWillStart, useState } from "@odoo/owl";
import { rpc } from "@web/core/network/rpc";




export class StudentScreen extends Component {
    static template = "college.student_profile_client";
    setup() {
        this.state = useState({'data': []})
        onWillStart(async () => {
            try {
                const data = await fetch('http://jsonplaceholder.typicode.com/users')
                const raw_data = await data.json()
                this.state.data = raw_data
            } catch(err) {
                console.log(err)
            }
        })
        this.onClickJump = () => {
            console.log('Button clicked!');
        };
    }

}

registry.category("actions").add("college.student_profile", StudentScreen);