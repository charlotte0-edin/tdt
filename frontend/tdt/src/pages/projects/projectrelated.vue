<template>
  <q-page padding>
    <leftDrawer />
    <div>
        <h5>{{ getProjectName() }} - Related Projects</h5>
    </div>
    <template>
  <div class="q-pa-md">
    <q-table
      :data="relatedProjects"
      :columns="columns"
      :visible-columns="visibleColumns"
      row-key="id"
    >
      <template v-slot:body-cell-delete="cellProperties">
          <q-td :props="cellProperties">
              <q-btn class="glossy" rounded color="indigo-12" label="Delete" @click="deleteRow(cellProperties.value)"/>
          </q-td>
      </template>
    </q-table>
  </div>
  <div>
    <q-btn class="glossy" rounded color="indigo-12" label="Add New" @click="showAdd = true"/>
  </div>

  <q-dialog v-model="showAdd" persistent>
      <addRelatedProject @close="closeDialogs()" @postFinished="refreshGrid()"/>
    </q-dialog>

</template>

  </q-page>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  data: () => ({
    visibleColumns: ['identifier', 'name', 'delete'],
    props: ['identifier', 'name'],
    columns: [
      {
        name: 'id',
        label: 'Id',
        field: 'Id',
        align: 'left',
        visible: 'false'
      },
      {
        name: 'identifier',
        label: 'Project ID',
        field: 'ProjectIdentifier',
        align: 'left'
      },
      {
        name: 'name',
        label: 'Name',
        field: 'ProjectName',
        align: 'left'
      },
      {
        name: 'delete',
        label: 'Delete',
        field: 'Id',
        align: 'right'
      }
    ],
    showAdd: false,
    showEdit: false,
    changeFlag: 0
  }),
  created () {
    if (!this.$store.getters['projects/getCurrentProject'].ProjectName) {
      this.$store.dispatch('projects/loadProjectDetails', this.$q.localStorage.getItem('selectedProjectId'))
    }
  },
  mounted () {
    if (!this.$store.getters['users/user']) {
      this.$router.push('/notuser')
    } else {
      if (!this.$store.getters['users/user'].Email) {
        this.$router.push('/notuser')
      }
    }
    this.$store.dispatch('relatedProjects/loadRelatedProjects', this.$q.localStorage.getItem('selectedProjectId'))
  },
  computed: {
    ...mapGetters('relatedProjects', ['relatedProjects'])
  },
  methods: {
    deleteRow (rowId) {
      if (confirm('Are you sure you want to remove this relationship from the project?')) {
        confirm('params: { id:' + rowId + ' }')
        this.$store.dispatch('relatedProjects/deleteRelatedProject', rowId)
      } else {
        confirm('Delete cancelled')
      }
    },
    closeDialogs: function () {
      this.showAdd = false
      this.showEdit = false
    },
    getProjectName () {
      return this.$store.getters['projects/getCurrentProject'].ProjectName
    }
  },
  components: {
    'addRelatedProject': require('components/Modals/ProjectPages/addRelatedProject.vue').default,
    'leftDrawer': require('components/projectLeftDrawer.vue').default
  }
}

</script>
