<template>
    <q-card style="min-width: 350px">
        <modal-header>Add New Category</modal-header>

        <form @submit.prevent="submitForm">
            <modal-name
            :Name.sync="categoryToAdd.CategoryName"
            ref="modalCatName"></modal-name>

            <modal-highlevel :Selected.sync="categoryToAdd.HighLevelCategory"></modal-highlevel>

            <modal-buttons />
        </form>
    </q-card>

</template>

<script>
export default {
  data () {
    return {
      categoryToAdd: {
        CategoryName: '',
        HighLevelCategory: false
      }
    }
  },
  methods: {
    submitForm () {
      this.$refs.modalCatName.$refs.Name.validate()
      if (!this.$refs.modalCatName.$refs.Name.hasError) {
        this.saveCategory()
        this.$emit('close')
      }
    },
    async saveCategory () {
      this.$store.dispatch('categories/addCategory', { item: this.categoryToAdd })
    }
  },
  components: {
    'modal-header': require('components/Modals/Shared/modalHeader.vue').default,
    'modal-name': require('components/Modals/Shared/modalSettingName.vue').default,
    'modal-highlevel': require('components/Modals/Shared/modalCheckbox.vue').default,
    'modal-buttons': require('components/Modals/Shared/modalButtons.vue').default
  }
}
</script>
