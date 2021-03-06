<template>
  <q-page padding>
    <leftDrawer />
    <template>
  <div class="q-pa-md">
    <q-table
      grid
      title="Project Officers"
      :data="projectOfficers"
      :columns="columns"
      row-key="Id"
      :filter="filter"
      hide-header
    >
      <template v-slot:top-right>
        <q-input borderless dense debounce="300" v-model="filter" placeholder="Search">
          <template v-slot:append>
            <q-icon name="search" />
          </template>
        </q-input>
      </template>

      <template v-slot:item="props">
        <div
          class="q-pa-xs col-xs-12 col-sm-6 col-md-4 col-lg-3 grid-style-transition"
          :style="props.selected ? 'transform: scale(0.95);' : ''"
        >
          <q-card :class="props.selected ? 'bg-grey-2' : ''">
            <q-card-section>
              {{ props.row.FirstName + ' ' + props.row.LastName }}
            </q-card-section>
            <q-separator />
            <q-list dense>
              <q-item v-for="col in props.cols.filter(col => col.name !== 'Id' && col.name !== 'firstName' && col.name !== 'lastName')" :key="col.name">
                <q-item-section>
                  <q-item-label>{{ col.label }}</q-item-label>
                </q-item-section>
                <q-item-section side>
                  <q-item-label caption>{{ col.value }}</q-item-label>
                </q-item-section>
              </q-item>
            </q-list>
            <q-separator />
            <q-card-section>
              <q-btn class="glossy" rounded color="indigo-12" label="Edit" align="left" @click="showEditDialog(props.row.Id)"/>
              <q-btn class="glossy" rounded color="indigo-12" label="Delete" align="right" @click="deleteRow(props.row.Id)"/>
            </q-card-section>
          </q-card>
        </div>
      </template>
    </q-table>
  </div>
  <div>
    <q-btn class="glossy" rounded color="indigo-12" label="Add New" @click="showAdd = true"/>
  </div>

  <q-dialog v-model="showAdd" persistent>
      <addOfficer @close="closeDialogs()" @postFinished="refreshGrid()"/>
    </q-dialog>

    <q-dialog v-model="showEdit" persistent>
        <editOfficer
        :officer="selectedOfficer">
        </editOfficer>
      </q-dialog>
</template>
  </q-page>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  data: () => ({
    selectedOfficer: {},
    columns: [
      {
        name: 'Id',
        label: 'Id',
        field: 'Id'
      },
      {
        name: 'firstName',
        label: 'First Name',
        field: 'FirstName'
      },
      {
        name: 'lastName',
        label: 'Last Name',
        field: 'LastName'
      },
      {
        name: 'address1',
        label: 'Address 1',
        field: 'Address1'
      },
      {
        name: 'address2',
        label: 'Address 2',
        field: 'Address2'
      },
      {
        name: 'address3',
        label: 'Address 3',
        field: 'Address3'
      },
      {
        name: 'town',
        label: 'Town',
        field: 'Town'
      },
      {
        name: 'county',
        label: 'County',
        field: 'County'
      },
      {
        name: 'tel',
        label: 'Telephone',
        field: 'Tel'
      },
      {
        name: 'mobile',
        label: 'Mobile',
        field: 'Mobile'
      },
      {
        name: 'email',
        label: 'Email',
        field: 'Email'
      }
    ],
    showAdd: false,
    showEdit: false
  }),
  methods: {
    deleteRow (rowId) {
      if (confirm('Are you sure you want to delete project officer with ID ' + rowId + '?')) {
        this.$store.dispatch('projectOfficers/deleteProjectOfficer', rowId)
      } else {
        alert('Delete cancelled')
      }
    },
    closeDialogs: function () {
      this.showAdd = false
      this.showEdit = false
    },
    showEditDialog: function (rowValue) {
      this.selectedOfficer = this.$store.getters['projectOfficers/getProjectOfficerById'](rowValue)
      this.showEdit = true
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
    this.$store.dispatch('projectOfficers/loadProjectOfficers')
  },
  computed: {
    ...mapGetters('projectOfficers', ['projectOfficers'])
  },
  components: {
    'addOfficer': require('components/Modals/addProjectOfficer.vue').default,
    'editOfficer': require('components/Modals/editProjectOfficer.vue').default,
    'leftDrawer': require('components/plainLeftDrawer.vue').default
  }
}
</script>
