<template>
  <q-page padding>
    <leftDrawer />
    <template>
  <div class="q-pa-md">
    <q-table
      title="Search Results"
      :data="searchResults"
      :columns="columns"
      :visible-columns="visibleColumns"
      row-key="id"
    >
      <template v-slot:body-cell-view="cellProperties">
          <q-td :props="cellProperties">
              <q-btn class="glossy" rounded color="indigo-12" label="View" @click="viewProject(cellProperties.value)"/>
          </q-td>
      </template>
    </q-table>
  </div>

</template>

  </q-page>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  data: () => ({
    visibleColumns: ['name', 'view'],
    props: ['id', 'name', 'view'],
    selectedCategory: {},
    columns: [
      {
        name: 'id',
        label: 'Id',
        field: 'Id',
        align: 'left'
      },
      {
        name: 'name',
        label: 'Name',
        field: 'ProjectName',
        align: 'left'
      },
      {
        name: 'view',
        label: 'View',
        field: 'Id',
        align: 'right'
      }
    ]
  }),
  mounted () {
    if (!this.$store.getters['users/user']) {
      this.$router.push('/notuser')
    } else {
      if (!this.$store.getters['users/user'].Email) {
        this.$router.push('/notuser')
      }
    }
    this.$store.dispatch('projects/searchProjects', this.$q.localStorage.getItem('searchParams'))
  },
  computed: {
    ...mapGetters({
      searchResults: 'projects/searchResults'
    })
  },
  methods: {
    viewProject (rowId) {
      this.$q.localStorage.set('selectedProjectId', rowId)
      this.$router.push('/project/details')
    }
  },
  components: {
    'leftDrawer': require('components/plainLeftDrawer.vue').default
  }
}

</script>
