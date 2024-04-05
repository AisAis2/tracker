<template> 
    <div class="is-flex-direction-column ml-5 mt-5 is-family-monospace">
        <nav class="breadcrumb" aria-label="breadcrumbs">
            <ul>
                <li><a href="/">Home</a></li>
                <li class="is-active"><a href="#" aria-current="page">Projects</a></li>
            </ul>
        </nav>
        <div class="is-flex">
            <p class="is-size-2 mr-1">User Management</p>
        </div>
        <table class="table">
            <thead>
                <th :style="{'width':'250px'}">Position</th>
                <th :style="{'width':'250px'}">Name</th>
                <th :style="{'width':'250px'}">Email</th>
                <th :style="{'width':'250px'}">Actions</th>
            </thead>
            <tbody>
                <tr v-for="user in userList">
                    <td>User</td>
                    <td>{{ user.username }}</td>
                    <td v-if="user.email">{{user.email}}</td>
                    <td v-else>{{ user.username }}@tracker.com</td>
                    <td>
                        <button class="button is-outlined is-small is-info has-text-weight-bold" data-target="modal-del" aria-haspopup='true'>
                            <span>Change Role</span>
                        </button>
                    </td>
                </tr>
            </tbody>
        </table>
        
    </div>
</template>

<script>
export default{
    computed:{
        userList(){
            return this.$store.state.user_list
        }
    }
}
</script>