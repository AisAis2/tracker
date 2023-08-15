<template>
    <div :class="{'is-active':isActive,'modal':true}" id='modal-ter'>
        <div class="modal-background"></div>
            <div class="modal-card">
                <header class="modal-card-head">
                    <p class="modal-card-title">Modal title</p>
                    <button class="delete" aria-label="close" @click="isActive=false"></button>
                </header>
                <section class="modal-card-body">

                </section>
            </div>
    </div>
</template>

<script>
export default {
    name:'EditProject',
    props:{
        project:Object
    }
}
</script>